import logging

from abc import ABC

from tornado.web import RequestHandler
from typeguard import typechecked


class AuthenticationPayload(ABC):
    """Payload used for authentication."""


class UsernamePasswordAuthenticationPayload(AuthenticationPayload):
    """An authentication payload comprised of Username and Password."""


class Authenticator():
    """An authenticator service."""

    _name: str = None

    @typechecked()
    def __init__(self, name: str, logger: logging.Logger):
        self._name = name
        self._logger = logger
        self._logger.info(f"Authenticator {self._name} created!")

    @property
    def name(self):
        return self._name

    @typechecked()
    def authenticate(self, handler: RequestHandler):
        """Authenticate a request."""
        self._logger.fatal("Not implemented!")
        raise NotImplemented()
