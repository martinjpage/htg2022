from src.services.csv_store_configuration import csv_store_configuration
from src.persistence.csv_store import CSVStore
import src.services.constants as const

from src.models.create_user import create_user


def command_main(args):
    config = csv_store_configuration()
    datastore = CSVStore(config)

    if args[const.action] == const.signup:
        create_user(args[const.username], args[const.password], args[const.location], datastore)
