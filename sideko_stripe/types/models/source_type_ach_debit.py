import pydantic
import typing


class SourceTypeAchDebit(pydantic.BaseModel):
    """
    SourceTypeAchDebit
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
