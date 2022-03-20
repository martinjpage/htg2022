from src.persistence.verification import verify_user, verify_password, verify_role, verify_active_dates
from src.models.smart_contract import execute_smart_contract
import src.services.constants as const


def create_offer(username, password, role, energy, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    if not verify_active_dates(username, datastore):
        raise ValueError("Account is not active. Check dates.")
    if not verify_role(username, role, datastore):
        raise ValueError(f"You have the incorrect role to perform this transaction. You need to be a {role}.")

    meter_id = datastore.get_meter_id(username)
    location = datastore.get_location(username)
    price = datastore.get_price(username)
    end_date = datastore.get_end_date(username)
    datastore.add_offer(meter_id, location, role, energy, price, end_date)


def execute_offer(args, role, datastore, matcher):
    create_offer(args[const.username], args[const.password], role, args[const.energy], datastore)
    match = matcher.match_offers()
    while bool(match):
        execute_smart_contract(match, datastore)
        match = matcher.match_offers()


def view_transaction_history(username, password, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    datastore.view_history(username)
