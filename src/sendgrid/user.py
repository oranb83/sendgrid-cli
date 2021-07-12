import logging

from src.sendgrid.base import SendGrid
from src.utils.common import log_error

logger = logging.getLogger(__name__)


class Teammate(SendGrid):
    """
    This class deals with SendGrid teammate (=> system users).
    """
    @log_error
    def get_all_teammates(self, is_admin=None):
        """
        Get all users.

        @type is_admin: bool or None
        @param is_admin: filters False for non admins, True for admins and None for all.
        @rtype: list<dict>
        @return: all users without access scopes
        """
        response = self.sendgrid_client.teammates.get().to_dict['result']
        if is_admin is not None:
            response = [item for item in response if item['is_admin'] == is_admin]

        return response

    @log_error
    def get_teammate(self, username):
        """
        Get a single users.

        @type username: str
        @param username: teammate username
        @rtype: dict
        @return: a single user with access scopes
        """
        response = self.sendgrid_client.teammates._(username).get()
        return response.to_dict

    @log_error
    def create_teammate(self, email, scopes=[], is_admin=False):
        """
        Update a single users.

        @type username: str
        @param username: teammate username
        @type scopes: list<str>
        @param scopes: list of access scopes
        @type is_admin: bool
        @param is_admin: user is admin or not
        @rtype: dict
        @return: a single user with access scopes
        """
        if is_admin:
            scopes = []
            logger.warning('Teammate with email %s will be set as admin', email)

        data = {
            'email': email,
            'scopes': scopes,
            'is_admin': is_admin
        }
        response = self.sendgrid_client.teammates.post(request_body=data)

        return response.to_dict

    @log_error
    def delete_teammate(self, username):
        """
        Delete a single users.

        @type username: str
        @param username: teammate username
        @rtype: dict
        @return: a single user with access scopes
        """
        self.sendgrid_client.teammates._(username).delete()
