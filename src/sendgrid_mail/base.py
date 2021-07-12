from sendgrid import SendGridAPIClient

from src.settings import SENDGRID_API_KEY_PRODUCTION, SENDGRID_API_KEY_STAGING


class SendGrid:
    def __init__(self, is_production, impersonate_subuser=None):
        """
        @type is_production: bool
        @param is_production: production or staging
        @type impersonate_subuser: str or None
        @param impersonate_subuser: None for root account, otherwise set subaccount by its username
        """
        if is_production or impersonate_subuser is not None:  # subusers must use the root api key
            api_key = SENDGRID_API_KEY_PRODUCTION
        else:
            api_key = SENDGRID_API_KEY_STAGING

        self.sendgrid_client = SendGridAPIClient(
            api_key=api_key, impersonate_subuser=impersonate_subuser).client
