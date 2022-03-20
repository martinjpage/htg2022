import re
import pandas as pd
import numpy as np
import datetime as dt

from src.domain.datastore_facade import DataStoreFacade


class CSVStore(DataStoreFacade):
    def __init__(self, config):
        self._config = config

    def add_user(self, username, password, meter_id, location):
        df = self._read_user_database()
        new_row = {self._config.username: username, self._config.password: password, self._config.meter_id: meter_id,
                   self._config.location: location}
        self._write_row_to_df(df, new_row, self._config.user_database)
        print(f"New user with id '{username}' and meter id '{meter_id}' added to user database.")

    def get_all_usernames(self) -> np.array:
        """Return array of all usernames in the user database"""
        df = self._read_user_database()
        return df[self._config.username].values

    def get_password(self, username):
        user_details = self._get_user_details(username)
        return user_details[self._config.password].values[0]

    def get_all_id(self) -> np.array:
        df = self._read_user_database()
        return df[self._config.meter_id].values

    def update_user_settings(self, username, role, price, state_date, end_date):
        df = self._read_user_database()
        df.loc[df[self._config.username] == username, self._config.role] = role
        df.loc[df[self._config.username] == username, self._config.price] = price
        df.loc[df[self._config.username] == username, self._config.start_date] = state_date
        df.loc[df[self._config.username] == username, self._config.end_date] = end_date
        df.to_csv(self._config.user_database, index=False)
        print(f"Role ({role}), price ({price}), start ({state_date}) and end ({end_date}) date updated for {username}.")

    def view_settings(self, username):
        user_details = self._get_user_details(username)
        print(user_details)

    def get_role(self, username):
        user_details = self._get_user_details(username)
        return user_details[self._config.role].values[0]

    def get_active_dates(self, username):
        user_details = self._get_user_details(username)
        start_date = user_details[self._config.start_date].values[0]
        start_date = dt.datetime.strptime(re.sub('[\.\:\-]', '/', start_date), '%Y/%m/%d').date()
        end_date = self._get_end_date(user_details)
        end_date = None if np.isnan(end_date) else dt.datetime.strptime(
            re.sub('[\.\:\-]', '/', end_date), '%Y/%m/%d').date()
        return start_date, end_date

    def get_end_date(self, username):
        user_details = self._get_user_details(username)
        return self._get_end_date(user_details)

    def _get_end_date(self, user_details):
        return user_details[self._config.end_date].values[0]

    def get_price(self, username):
        user_details = self._get_user_details(username)
        return user_details[self._config.price].values[0]

    def get_meter_id(self, username):
        user_details = self._get_user_details(username)
        return user_details[self._config.meter_id].values[0]

    def get_location(self, username):
        user_details = self._get_user_details(username)
        return user_details[self._config.location].values[0]

    def add_offer(self, meter_id, location, role, energy, price, end_date):
        df = self._read_orderbook()
        new_row = {self._config.meter_id: meter_id, self._config.location: location, self._config.role: role,
                   self._config.energy: energy, self._config.price: price, self._config.end_date: end_date}
        self._write_row_to_df(df, new_row, self._config.orderbook)
        print(f"New {role} offer from {meter_id} added to orderbook.")

    def view_history(self, username):
        df = self._read_ledger()
        buyer_history_mask = df[self._config.buyer] == username
        if not buyer_history_mask.any():
            print("No buyer history.")
        else:
            print("Buyer History:")
            print(df[buyer_history_mask])

        supplier_history_mask = df[self._config.supplier] == username
        if not supplier_history_mask.any():
            print("No seller history.")
        else:
            print("Supplier History:")
            print(df[supplier_history_mask])

    def read_orderbook(self):
        return self._read_orderbook()

    def update_orderbook(self, total_energy, supplier_index, buyer_index):
        df = self._read_orderbook()
        df.at[supplier_index, self._config.energy] -= total_energy
        df.at[buyer_index, self._config.energy] -= total_energy
        zero_rows = df[self._config.energy] == 0
        if zero_rows.any():
            print('Removing fulfilled orders from orderbook:', '\n', df[zero_rows])
        df = df[~zero_rows]
        df.to_csv(self._config.orderbook, index=False)

    def record_on_ledger(self, buyer, supplier, unit_price, total_price, energy):
        total_price = round(total_price, 2)
        energy = round(energy, 2)
        today = dt.date.today()
        df = self._read_ledger()
        new_row = {self._config.buyer: buyer, self._config.supplier: supplier, self._config.price: unit_price,
                   self._config.energy: energy, self._config.total_price: total_price, self._config.date: today}
        self._write_row_to_df(df, new_row, self._config.ledger_history)
        print(f"Recorded transaction between {buyer} (buyer) and {supplier} (supplier) for {energy} kWh at"
              f" {unit_price} EUR per kWh (total: {total_price:.2f} EUR).")

    def _read_user_database(self) -> pd.DataFrame:
        return pd.read_csv(self._config.user_database)

    def _get_user_details(self, username):
        df = self._read_user_database()
        return df[df[self._config.username] == username]

    def _read_orderbook(self) -> pd.DataFrame:
        return pd.read_csv(self._config.orderbook)

    def _read_ledger(self) -> pd.DataFrame:
        return pd.read_csv(self._config.ledger_history)

    def _write_row_to_df(self, df, new_row, path):
        new_row = pd.DataFrame([new_row], columns=new_row.keys())
        df = pd.concat([df, new_row], axis=0)
        df.to_csv(path, index=False)
