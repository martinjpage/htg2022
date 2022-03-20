from src.domain.smart_device import SmartDevice


class SmartWallet(SmartDevice):

    def update_balance(self, requested_amount, username):
        print(f"{username}'s wallet balanced updated by {requested_amount:.2f} EUR.")
