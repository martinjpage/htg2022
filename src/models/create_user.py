from src.persistence.verification import verify_user


def create_user(username, password, location, data_store):
    if verify_user(username, data_store):
        raise ValueError(f'A user with name "{username}" already exists')
    data_store.add_user(username, password, location)
