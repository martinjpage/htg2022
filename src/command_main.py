from src.services.csv_store_configuration import csv_store_configuration
from src.persistence.csv_store import CSVStore
import src.services.constants as const

from src.models.create_user import create_user
from src.models.settings import update_user_settings, view_settings
from src.models.transactions import create_offer, view_transaction_history
from src.models.matcher import match_offers
from src.models.smart_contract import execute_smart_contract


def command_main(args):
    config = csv_store_configuration()
    datastore = CSVStore(config)

    if args[const.action] == const.signup:
        create_user(args[const.username], args[const.password], args[const.location], datastore)

    elif args[const.action] == const.update_settings:
        update_user_settings(args[const.username], args[const.password], args[const.role], args[const.price],
                             args[const.start], args[const.end], datastore)

    elif args[const.action] == const.view_settings:
        view_settings(args[const.username], args[const.password], datastore)

    elif args[const.action] == const.supplier:
        create_offer(args[const.username], args[const.password], const.supplier, args[const.energy], datastore)
        match = match_offers(datastore)
        if match:
            execute_smart_contract(match, datastore)

    elif args[const.action] == const.buyer:
        create_offer(args[const.username], args[const.password], const.buyer, args[const.energy], datastore)
        match = match_offers(datastore)
        if match:
            execute_smart_contract(match, datastore)

    elif args[const.action] == const.history:
        view_transaction_history(args[const.username], args[const.password], datastore)
