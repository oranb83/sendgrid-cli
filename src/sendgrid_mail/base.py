from sendgrid import SendGridAPIClient

from src.settings import SENDGRID_API_KEY_PRODUCTION


class SendGrid:
    def __init__(self, impersonate_subuser=None):
        """
        @type impersonate_subuser: str or None
        @param impersonate_subuser: None for root account, otherwise set subaccount by its username
        """
        api_key = SENDGRID_API_KEY_PRODUCTION
        self.sendgrid_client = SendGridAPIClient(
            api_key=api_key, impersonate_subuser=impersonate_subuser).client
