from src.domain.smart_device import SmartDevice


class SmartWallet(SmartDevice):

    def update_balance(self, requested_amount):
        print(f'Wallet balanced updated by {requested_amount} EUR.')
