from src.persistence.verification import verify_user, verify_id


def create_user(username, password, meter_id, location, data_store):
    if verify_user(username, data_store):
        raise ValueError(f'A user with name "{username}" already exists')
    if verify_id(meter_id, data_store):
        raise ValueError(f'A meter with meter id "{meter_id}" already exists')
    data_store.add_user(username, password, meter_id, location)
