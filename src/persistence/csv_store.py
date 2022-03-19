import pandas as pd
import numpy as np

from src.domain.datastore_facade import DataStoreFacade


class CSVStore(DataStoreFacade):
    def __init__(self, config):
        self._config = config

    def add_user(self, username, password, location):
        df = pd.read_csv(self._config.user_database)
        new_row = {self._config.username: username, self._config.password: password,  self._config.location: location}
        new_row = pd.DataFrame([new_row], columns=new_row.keys())
        df = pd.concat([df, new_row], axis=0)
        df.to_csv(self._config.user_database, index=False)
        print(f"New user with id '{username}' added to database.")

    def get_all_usernames(self) -> np.array:
        """Return array of all usernames in the user database"""
        df = pd.read_csv(self._config.user_database)
        return df[self._config.username].values

    def update_settings(self, username, role, price, state_date, end_date):
        pass

    def view_settings(self, username):
        pass

    def get_role(self):
        pass

    def get_active_dates(self, username):
        pass

    def get_end_date(self, username):
        pass

    def get_price(self, username):
        pass

    def add_offer(self, username, role, energy, price, end_date):
        pass

    def view_history(self, username):
        pass

    def update_orderbook(self):
        pass

    def record_on_blockchain(self):
        pass
