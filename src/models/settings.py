from src.persistence.verification import verify_user, verify_password


def update_user_settings(username, password, role, price, state_date, end_date, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    if end_date is not None and state_date > end_date:
        raise ValueError("Start date cannot occur after the end date.")
    datastore.update_user_settings(username, role, price, state_date, end_date)


def view_settings(username, password, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    datastore.view_settings(username)
