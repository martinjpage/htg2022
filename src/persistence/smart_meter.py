from src.domain.smart_device import SmartDevice


class SmartMeter(SmartDevice):

    def update_balance(self, requested_amount):
        print(f'Energy balanced updated by {requested_amount} kWh.')
