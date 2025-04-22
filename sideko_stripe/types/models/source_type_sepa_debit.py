import pydantic
import typing


class SourceTypeSepaDebit(pydantic.BaseModel):
    """
    SourceTypeSepaDebit
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    branch_code: typing.Optional[str] = pydantic.Field(
        alias="branch_code", default=None
    )
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    mandate_reference: typing.Optional[str] = pydantic.Field(
        alias="mandate_reference", default=None
    )
    mandate_url: typing.Optional[str] = pydantic.Field(
        alias="mandate_url", default=None
    )
