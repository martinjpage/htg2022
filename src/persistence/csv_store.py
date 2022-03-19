import pandas as pd
import numpy as np

from src.domain.datastore_facade import DataStoreFacade


class CSVStore(DataStoreFacade):
    def __init__(self, config):
        self._config = config

    def add_user(self, username, password, location):
        df = self._read_user_database()
        new_row = {self._config.username: username, self._config.password: password,  self._config.location: location}
        new_row = pd.DataFrame([new_row], columns=new_row.keys())
        df = pd.concat([df, new_row], axis=0)
        df.to_csv(self._config.user_database, index=False)
        print(f"New user with id '{username}' added to database.")

    def get_all_usernames(self) -> np.array:
        """Return array of all usernames in the user database"""
        df = self._read_user_database()
        return df[self._config.username].values

    def get_password(self, username):
        df = self._read_user_database()
        return df[df[self._config.username] == username][self._config.password].values[0]

    def update_user_settings(self, username, role, price, state_date, end_date):
        df = self._read_user_database()
        df.loc[df[self._config.username] == username, self._config.role] = role
        df.loc[df[self._config.username] == username, self._config.price] = price
        df.loc[df[self._config.username] == username, self._config.start_date] = state_date
        df.loc[df[self._config.username] == username, self._config.end_date] = end_date
        df.to_csv(self._config.user_database, index=False)
        print(f"Role ({role}), price ({price}), start ({state_date}) and end ({end_date}) date updated for {username}.")

    def view_settings(self, username):
        df = self._read_user_database()
        print(df[df[self._config.username] == username])

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

    def _read_user_database(self) -> pd.DataFrame:
        return pd.read_csv(self._config.user_database)
