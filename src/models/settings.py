from src.persistence.verification import verify_user, verify_password


def update_user_settings(username, password, role, price, state_date, end_date, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    datastore.update_user_settings(username, role, price, state_date, end_date)


def view_settings(username, password, datastore):
    if not verify_user(username, datastore) or not verify_password(username, password, datastore):
        raise ValueError("Could not verify username and password")
    datastore.view_settings(username)
