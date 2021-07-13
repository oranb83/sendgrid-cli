import logging
import argparse

from src.sdk.sdk import *

SUBACCOUNTS = [
    'cross_platform',
    'car_company',
    'life_company',
    'pet_company',
    'home_company'
]

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)


class Main:
    """
    This class does the heavy lifting and controling all the possible commands
    """
    def __init__(self, args):
        self.dest_subaccount = args.dest_subaccount
        self.add_sendgrid_users = args.add_sendgrid_users

    def run(self):
        if self.dest_subaccount not in SUBACCOUNTS:
            raise Exception(
                f'Sub account {self.dest_subaccount} is illegal, please use one of these sub accounts: {SUBACCOUNTS}')

        return add_sendgrid_users_to_subaccounts(
            self.add_sendgrid_users, self.dest_subaccount)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('SendGrid Users')
    parser.add_argument('--dest_subaccount', required=True, help='Destination_subaccount')
    parser.add_argument('--add_sendgrid_users', nargs='+', required=True, help='Add new sendgrid user')

    args = parser.parse_args()

    Main(args).run()
