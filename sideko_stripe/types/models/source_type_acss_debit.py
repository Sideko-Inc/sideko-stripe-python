import pydantic
import typing


class SourceTypeAcssDebit(pydantic.BaseModel):
    """
    SourceTypeAcssDebit
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_address_city: typing.Optional[str] = pydantic.Field(
        alias="bank_address_city", default=None
    )
    bank_address_line_1: typing.Optional[str] = pydantic.Field(
        alias="bank_address_line_1", default=None
    )
    bank_address_line_2: typing.Optional[str] = pydantic.Field(
        alias="bank_address_line_2", default=None
    )
    bank_address_postal_code: typing.Optional[str] = pydantic.Field(
        alias="bank_address_postal_code", default=None
    )
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    category: typing.Optional[str] = pydantic.Field(alias="category", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
