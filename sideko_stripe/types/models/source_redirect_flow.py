import pydantic
import typing


class SourceRedirectFlow(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    failure_reason: typing.Optional[str] = pydantic.Field(
        alias="failure_reason", default=None
    )
    """
    The failure reason for the redirect, either `user_abort` (the customer aborted or dropped out of the redirect flow), `declined` (the authentication failed or the transaction was declined), or `processing_error` (the redirect failed due to a technical error). Present only if the redirect status is `failed`.
    """
    return_url: str = pydantic.Field(
        alias="return_url",
    )
    """
    The URL you provide to redirect the customer to after they authenticated their payment.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the redirect, either `pending` (ready to be used by your customer to authenticate the transaction), `succeeded` (succesful authentication, cannot be reused) or `not_required` (redirect should not be used) or `failed` (failed authentication, cannot be reused).
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL provided to you to redirect a customer to as part of a `redirect` authentication flow.
    """
