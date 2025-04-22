from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.reporting.report_run import (
    AsyncReportRunClient,
    ReportRunClient,
)
from sideko_stripe.resources.reporting.report_type import (
    AsyncReportTypeClient,
    ReportTypeClient,
)


class ReportingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.report_run = ReportRunClient(base_client=self._base_client)
        self.report_type = ReportTypeClient(base_client=self._base_client)


class AsyncReportingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.report_run = AsyncReportRunClient(base_client=self._base_client)
        self.report_type = AsyncReportTypeClient(base_client=self._base_client)
