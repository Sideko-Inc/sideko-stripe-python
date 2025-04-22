import pydantic
import typing


class SourceTypeMultibanco(pydantic.BaseModel):
    """
    SourceTypeMultibanco
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    entity: typing.Optional[str] = pydantic.Field(alias="entity", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    refund_account_holder_address_city: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_city", default=None
    )
    refund_account_holder_address_country: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_country", default=None
    )
    refund_account_holder_address_line1: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_line1", default=None
    )
    refund_account_holder_address_line2: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_line2", default=None
    )
    refund_account_holder_address_postal_code: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_postal_code", default=None
    )
    refund_account_holder_address_state: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_address_state", default=None
    )
    refund_account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="refund_account_holder_name", default=None
    )
    refund_iban: typing.Optional[str] = pydantic.Field(
        alias="refund_iban", default=None
    )
