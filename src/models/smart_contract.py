from src.persistence.verification import verify_supplier, verify_buyer
from src.persistence.smart_meter import SmartMeter
from src.persistence.smart_wallet import SmartWallet

supplier_smart_energy_meter = SmartMeter()
supplier_smart_wallet = SmartWallet()
buyer_smart_energy_meter = SmartMeter()
buyer_smart_wallet = SmartWallet()


def execute_smart_contract(match, datastore):
    total_price, total_energy = calculate_transaction(match['energy_available'], match['energy_requested'],
                                                      match['price'], match['supplier_username'], match['buyer_username'])
    if not verify_supplier(match['supplier_username'], total_energy, supplier_smart_energy_meter) or \
            not verify_buyer(match['buyer_username'], total_price, buyer_smart_wallet):
        raise ValueError("Could not verify buyer or supplier.")

    update_meters(total_energy, total_price, match['supplier_username'], match['buyer_username'])

    datastore.update_orderbook(total_energy, supplier_index=match['supplier_index'], buyer_index=match['buyer_index'])
    datastore.record_on_ledger(match['buyer_username'], match['supplier_username'], match['price'], total_price, total_energy)


def calculate_transaction(energy_available, energy_requested, price, supplier_username, buyer_username):
    if energy_available >= energy_requested:
        print(f"{supplier_username} can meet the full energy request from {buyer_username} of {energy_requested} kWh. "
              f"Transaction will occur at a unit price of {price} EUR.")
        total_price = energy_requested * price
        total_energy = energy_requested
        return total_price, total_energy

    elif energy_available < energy_requested:
        print(f"{supplier_username} can partially meet the request from {buyer_username} and supply {energy_available} kWh"
              f" of the requested {energy_requested} kWh. Transaction will occur at a unit price of {price} EUR.")
        total_price = energy_available * price
        total_energy = energy_available
        return total_price, total_energy


def update_meters(total_energy, total_price, supplier_username, buyer_username):
    supplier_smart_energy_meter.update_balance(-total_energy, supplier_username)
    buyer_smart_energy_meter.update_balance(total_energy, buyer_username)

    supplier_smart_wallet.update_balance(total_price, supplier_username)
    buyer_smart_wallet.update_balance(-total_price, buyer_username)
