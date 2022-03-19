import re
import argparse
from datetime import datetime

import src.services.constants as const
from src.command_main import command_main


def argument_collector():
    """Defines command line menu, parses arguments and returns namespace from argparse.ArgumentParser."""
    # general arguments for all parsers
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-un', f'--{const.username}', help="Input your username", type=str,
                             required=True)
    parent_parser.add_argument('-pw', f'--{const.password}', help="Input your password.", type=str, required=True)

    # main parser for access to different actions
    main_parser = argparse.ArgumentParser(description="Tool for matching peer-to-peer energy sales.")

    subparsers = main_parser.add_subparsers(help="Choose an action to create a new user ('signup'), update your"
                                                 "profile settings ('update_settings'), view your profile settings "
                                                 "('view_settings'), transact as a supplier ('supplier'), or"
                                                 "transact as a buyer ('buyer'), and view your transaction"
                                                 "history ('history').", dest=const.action)

    # arguments to create a new user
    create_user = subparsers.add_parser(const.signup, help="Create user profile.", parents=[parent_parser])
    create_user.add_argument('-l', f'--{const.location}', help="Choose a location.", type=str, choices=['Italy'], required=True)

    # arguments to update the user settings
    update_settings = subparsers.add_parser(const.update_settings, help="Select a role as supplier or buyer, set a price "
                                                                    "and a date range.", parents=[parent_parser])

    update_settings.add_argument('-r', f'--{const.role}', help="Choose to be a supplier or buyer.", type=str,
                             choices=['supplier', 'buyer'], required=True)
    update_settings.add_argument('-p', f'--{const.price}', help="Set your minimum sell price or maximum buy price (EUR)",
                                 type=float, required=True)
    update_settings.add_argument('-s', f'--{const.start}', help="Set the start date for transactions to run.",
                       type=lambda d: datetime.strptime(re.sub('[\.\:\/]', '-', d), '%Y-%m-%d'),
                       default=datetime.today().strftime('%Y-%m-%d'))
    update_settings.add_argument('-e', f'--{const.end}', help="Set the end date for transactions to run.",
                       type=lambda d: datetime.strptime(d, '%Y-%m-%d'), default=None)

    # argument to view user settings
    view_settings = subparsers.add_parser('view_settings', help="View your current role (supplier or buyer), price "
                                                                "and active date range.", parents=[parent_parser])

    # arguments to transact as a supplier
    supplier = subparsers.add_parser(const.supplier, help="Perform a sell transaction as a supplier.",
                                     parents=[parent_parser])

    supplier.add_argument('-e', f'--{const.energy}', help="Give the amount of energy you want to sell in kWh.", 
                          type=float, required=True)

    # arguments to transact as a buyer
    buyer = subparsers.add_parser(const.buyer, help="Perform a buy transaction as a buyer.")

    buyer.add_argument('-e', f'--{const.energy}', help="Give the amount of energy you want to buy in kWh.", type=float,
                       required=True)

    # argument to view transaction history
    history = subparsers.add_parser(const.history, help="View block chain transaction history.", parents=[parent_parser])

    return vars(main_parser.parse_args())


if __name__ == '__main__':
    # args = argument_collector()
    # print(args)
    args = {'action': 'signup', 'username': 'mjp5', 'password': 'ab12', 'location': 'Italy'}
    command_main(args)
