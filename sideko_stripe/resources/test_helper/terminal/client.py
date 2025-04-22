from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.test_helper.terminal.reader import (
    AsyncReaderClient,
    ReaderClient,
)


class TerminalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.reader = ReaderClient(base_client=self._base_client)


class AsyncTerminalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.reader = AsyncReaderClient(base_client=self._base_client)
