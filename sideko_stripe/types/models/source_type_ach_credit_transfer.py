import pydantic
import typing


class SourceTypeAchCreditTransfer(pydantic.BaseModel):
    """
    SourceTypeAchCreditTransfer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    refund_account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_name", default=None
    )
    refund_account_holder_type: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_type", default=None
    )
    refund_routing_number: typing.Optional[str] = pydantic.Field(
        alias="refund_routing_number", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    swift_code: typing.Optional[str] = pydantic.Field(alias="swift_code", default=None)
