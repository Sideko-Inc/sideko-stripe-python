import pydantic
import typing


class IssuingAuthorizationNetworkData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acquiring_institution_id: typing.Optional[str] = pydantic.Field(
        alias="acquiring_institution_id", default=None
    )
    """
    Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`.
    """
    system_trace_audit_number: typing.Optional[str] = pydantic.Field(
        alias="system_trace_audit_number", default=None
    )
    """
    The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the acquirer. Prefer `network_data.transaction_id` if present, unless you have special requirements.
    """
    transaction_id: typing.Optional[str] = pydantic.Field(
        alias="transaction_id", default=None
    )
    """
    Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.
    """
