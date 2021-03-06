from src.domain.smart_device import SmartDevice


class SmartMeter(SmartDevice):

    def update_balance(self, requested_amount, username):
        print(f"{username}'s energy balanced updated by {requested_amount:.2f} kW.")
