"""Exceptions which used in Apps."""

from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    """ Base API Exception to provide option to fail silently"""
    send_to_sentry = True

    def __init__(self, *args, **kwargs):
        if 'send_to_sentry' in kwargs:
            self.send_to_sentry = kwargs.pop('send_to_sentry')
        super(BaseAPIException, self).__init__(*args, **kwargs)


class UnauthorizedAccess(BaseAPIException):
    """user Authorization failed."""

    status_code = 401
    default_detail = 'User is not authorized to access.'
    default_code = 'unauthorized_access'
    send_to_sentry = False
