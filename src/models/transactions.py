from src.persistence.verification import verify_user, verify_password, verify_role, verify_active_dates


def create_offer(username, password, role, energy, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    if not verify_active_dates(username, datastore):
        raise ValueError("Account is not active. Check dates.")
    if not verify_role(username, role, datastore):
        raise ValueError(f"You have the incorrect role to perform this transaction. You need to be a {role}.")

    location = datastore.get_location(username)
    price = datastore.get_price(username)
    end_date = datastore.get_end_date(username)
    datastore.add_offer(username, location, role, energy, price, end_date)


def view_transaction_history(username, password, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    datastore.view_history(username)
