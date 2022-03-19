import os
from collections import namedtuple


def csv_store_configuration():
    user_database = os.path.join("databases", "user_database.csv")
    orderbook = os.path.join("databases", "orderbook.csv")
    blockchain_history = os.path.join("databases", "blockchain_history.csv")

    paths = {'user_database': user_database, 'orderbook': orderbook, 'blockchain_history': blockchain_history}
    user_database_columns = {"username": "username", "password": 'password', "location": "location", "role": "role",
                             "price": "price", "start_date": "start_date", "end_date": "end_date"}

    all_keys = paths | user_database_columns
    return namedtuple('configuration', all_keys.keys())(**all_keys)
