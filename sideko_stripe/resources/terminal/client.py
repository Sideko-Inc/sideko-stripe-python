from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.terminal.configuration import (
    AsyncConfigurationClient,
    ConfigurationClient,
)
from sideko_stripe.resources.terminal.connection_token import (
    AsyncConnectionTokenClient,
    ConnectionTokenClient,
)
from sideko_stripe.resources.terminal.location import (
    AsyncLocationClient,
    LocationClient,
)
from sideko_stripe.resources.terminal.reader import AsyncReaderClient, ReaderClient


class TerminalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.configuration = ConfigurationClient(base_client=self._base_client)
        self.location = LocationClient(base_client=self._base_client)
        self.reader = ReaderClient(base_client=self._base_client)
        self.connection_token = ConnectionTokenClient(base_client=self._base_client)


class AsyncTerminalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.configuration = AsyncConfigurationClient(base_client=self._base_client)
        self.location = AsyncLocationClient(base_client=self._base_client)
        self.reader = AsyncReaderClient(base_client=self._base_client)
        self.connection_token = AsyncConnectionTokenClient(
            base_client=self._base_client
        )
