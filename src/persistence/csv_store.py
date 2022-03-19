from src.domain.datastore_facade import DataStoreFacade


class CSVStore(DataStoreFacade):
    def __init__(self, config):
        self._config = config

    def add_user(self, username, password, location):
        pass

    def get_all_user_credentials(self):
        pass

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
