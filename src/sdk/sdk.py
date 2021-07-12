import logging

from src.sendgrid_mail.user import Teammate as SendgridUser
from src.settings import BASE_SCOPES

ID = 'id'
SUBACCOUNTS = ['cross_platform', 'car_company', 'life_company', 'pet_company', 'home_company']
SENGRID_TEMPLATES_MIGRATED_NAMES_FILE = 'templates_subaccounts_migrated_names.csv'

logger = logging.getLogger(__name__)


def add_sendgrid_users_to_subaccounts(emails, dest_subaccount, is_admin=False):
    """
    Migrate sendgrid users based on a csv that contains columns: `username`, `subaccounts`.

    @type emails: list<str>
    @param emails: emails to add to a new subaccount
    @type dest_subaccount: str
    @param dest_subaccount: destination subaccount
    """
    subaccount = SendgridUser(True, impersonate_subuser=dest_subaccount)

    for email in emails:
        try:
            logger.info('Starting to add user with email %s to subaccount %s', email,
                        dest_subaccount)
            subaccount.create_teammate(email, scopes=BASE_SCOPES, is_admin=is_admin)
            logger.info('Created user with email %s in subaccount %s', email, dest_subaccount)
        except Exception as e:
            logger.error('Failed creating user with email %s in subaccount %s', email, dest_subaccount)
            continue
