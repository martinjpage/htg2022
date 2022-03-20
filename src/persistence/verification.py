import datetime as dt


def verify_user(username: str, datastore):
    all_users = datastore.get_all_usernames()
    if len(all_users) == 0:
        return False
    return username in all_users

def verify_id(meter_id, datastore):
    all_id = datastore.get_all_id()
    if len(all_id) == 0:
        return False
    return meter_id in all_id


def verify_password(username: str, password: str, datastore):
    user_password = datastore.get_password(username)
    return password == user_password


def verify_active_dates(username, datastore):
    start_date, end_date = datastore.get_active_dates(username)
    today = dt.date.today()
    return today >= start_date and (end_date is None or end_date >= today)


def verify_role(username, role, datastore):
    user_role = datastore.get_role(username)
    return user_role == role


def verify_smart_device(username, requested_amount, smart_device):
    return smart_device.authentiate(username) and smart_device.check_balance(requested_amount)


def verify_supplier(username, energy_request, smart_meter):
    if verify_smart_device(username, energy_request, smart_meter):
        print("Seller authenticated. Energy available.")
        return True


def verify_buyer(username, wallet_request, smart_wallet):
    if verify_smart_device(username, wallet_request, smart_wallet):
        print("Buyer authenticated. Money available.")
        return True
