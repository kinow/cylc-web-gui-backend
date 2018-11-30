import logging

from auth import Authenticator
from dependency_injector import containers, providers


class IocContainer(containers.DeclarativeContainer):
    """Application IoC container."""

    #config = providers.Configuration('config')
    logger = providers.Singleton(logging.Logger, name='cylc.web')

    auth_service = providers.Factory(
        Authenticator,
        #token_ttl=config.auth.token_ttl,
        logger=logger,
        name="My Auth 1"
    )
