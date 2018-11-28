from abc import ABC

from tornado.web import RequestHandler
from typeguard import typechecked


class AuthenticationPayload(ABC):
    """Payload used for authentication."""


class UsernamePasswordAuthenticationPayload(AuthenticationPayload):
    """An authentication payload comprised of Username and Password."""


class Authenticator():
    """An authenticator service."""

    name: str = None

    @typechecked()
    def __init__(self, name: str = None):
        self.name = name

    @typechecked()
    def authenticate(self, handler: RequestHandler):
        """Authenticate a request."""
