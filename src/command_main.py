from src.services.csv_store_configuration import csv_store_configuration
from src.persistence.csv_store import CSVStore



def command_main(args):
    config = csv_store_configuration()
    datastore = CSVStore(config)
