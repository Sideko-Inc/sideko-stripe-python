from sideko_stripe.core import AsyncBaseClient, SyncBaseClient
from sideko_stripe.resources.identity.verification_report import (
    AsyncVerificationReportClient,
    VerificationReportClient,
)
from sideko_stripe.resources.identity.verification_session import (
    AsyncVerificationSessionClient,
    VerificationSessionClient,
)


class IdentityClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.verification_report = VerificationReportClient(
            base_client=self._base_client
        )
        self.verification_session = VerificationSessionClient(
            base_client=self._base_client
        )


class AsyncIdentityClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.verification_report = AsyncVerificationReportClient(
            base_client=self._base_client
        )
        self.verification_session = AsyncVerificationSessionClient(
            base_client=self._base_client
        )
