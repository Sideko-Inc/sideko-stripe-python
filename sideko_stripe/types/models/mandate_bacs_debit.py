import pydantic
import typing
import typing_extensions


class MandateBacsDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    network_status: typing_extensions.Literal[
        "accepted", "pending", "refused", "revoked"
    ] = pydantic.Field(
        alias="network_status",
    )
    """
    The status of the mandate on the Bacs network. Can be one of `pending`, `revoked`, `refused`, or `accepted`.
    """
    reference: str = pydantic.Field(
        alias="reference",
    )
    """
    The unique reference identifying the mandate on the Bacs network.
    """
    revocation_reason: typing.Optional[
        typing_extensions.Literal[
            "account_closed",
            "bank_account_restricted",
            "bank_ownership_changed",
            "could_not_process",
            "debit_not_authorized",
        ]
    ] = pydantic.Field(alias="revocation_reason", default=None)
    """
    When the mandate is revoked on the Bacs network this field displays the reason for the revocation.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL that will contain the mandate that the customer has signed.
    """
