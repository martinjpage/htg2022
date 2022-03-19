

def verify_user(username: str, datastore):
    all_users = datastore.get_all_usernames()
    return username in all_users


def verify_password(username: str, password: str, datastore):
    user_password = datastore.get_password(username)
    return password == user_password
