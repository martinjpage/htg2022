import datetime as dt


def verify_user(username: str, datastore):
    all_users = datastore.get_all_usernames()
    if len(all_users) == 0:
        return False
    return username in all_users


def verify_password(username: str, password: str, datastore):
    user_password = datastore.get_password(username)
    return password == user_password


def verify_active_dates(username, datastore):
    start_date, end_date = datastore.get_active_dates(username)
    today = dt.date.today()
    return start_date >= today and (end_date is None or end_date >= today)


def verify_role(username, role, datastore):
    user_role = datastore.get_role(username)
    return user_role == role
