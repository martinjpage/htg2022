from abc import abstractmethod
import numpy as np


class SmartDevice:
    def __init__(self):
        self._balance = np.inf

    def authentiate(self, username):
        return username == username

    def check_balance(self, requested_amount):
        return requested_amount < self._balance

    @abstractmethod
    def update_balance(self, requested_amount):
        pass
