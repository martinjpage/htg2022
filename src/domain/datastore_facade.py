from abc import ABC, abstractmethod


class DataStoreFacade(ABC):
    @abstractmethod
    def add_user(self, username, password, location):
        pass

    @abstractmethod
    def get_all_usernames(self):
        pass

    @abstractmethod
    def update_settings(self, username, role, price, state_date, end_date):
        pass

    @abstractmethod
    def view_settings(self, username):
        pass

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_active_dates(self, username):
        pass

    @abstractmethod
    def get_end_date(self, username):
        pass

    @abstractmethod
    def get_price(self, username):
        pass

    @abstractmethod
    def add_offer(self, username, role, energy, price, end_date):
        pass

    @abstractmethod
    def view_history(self, username):
        pass

    @abstractmethod
    def update_orderbook(self):
        pass

    @abstractmethod
    def record_on_blockchain(self):
        pass
