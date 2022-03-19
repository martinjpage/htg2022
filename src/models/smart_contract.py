from src.persistence.verification import verify_supplier, verify_buyer
from src.persistence.smart_meter import SmartMeter
from src.persistence.smart_wallet import SmartWallet

seller_smart_energy_meter = SmartMeter()
seller_smart_wallet = SmartWallet()
buyer_smart_energy_meter = SmartMeter()
buyer_smart_wallet = SmartWallet()


def execute_smart_contract(match, datastore):
    if not verify_supplier(match['supplier_username'], match['energy_request'], seller_smart_energy_meter) and \
            not verify_buyer(match['buyer_username'], match['wallet_request'], buyer_smart_wallet):
        raise ValueError("Could not verify buyer or supplier.")

    seller_smart_energy_meter.update_balance(-match['energy_request'])
    buyer_smart_energy_meter.update_balance(match['energy_request'])

    seller_smart_wallet.update_balance(match['wallet_request'])
    buyer_smart_wallet.update_balance(-match['wallet_request'])

    datastore.update_orderbook()
    datastore.record_on_ledger(match['buyer_username'], match['supplier_username'], match['wallet_request'],
                               match['energy_request'])
