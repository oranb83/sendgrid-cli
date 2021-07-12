import logging

logger = logging.getLogger(__name__)


def log_error(func):
    """
    This decorator will log the actual error message from the failed request without changing it's
    logic.

    SendGrid responses raise exceptions instead of sending a response with error message and
    status.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            logger.error(e.to_dict)
            raise

    return wrapper
