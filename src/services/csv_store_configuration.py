import os
from collections import namedtuple


def csv_store_configuration():
    user_database = os.path.join("src", "databases", "user_database.csv")
    orderbook = os.path.join("src", "databases", "orderbook.csv")
    ledger_history = os.path.join("src", "databases", "ledger_history.csv")

    paths = {'user_database': user_database, 'orderbook': orderbook, 'ledger_history': ledger_history}
    database_columns = {"username": "username", "password": 'password', "location": "location", "role": "role",
                        "price": "price", "start_date": "start_date", "end_date": "end_date", "energy": "energy",
                        "buyer": "buyer", "supplier": "supplier", "total_price": "total_price", "date": "date"}

    all_keys = paths | database_columns
    return namedtuple('configuration', all_keys.keys())(**all_keys)
