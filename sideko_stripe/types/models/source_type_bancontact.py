import pydantic
import typing


class SourceTypeBancontact(pydantic.BaseModel):
    """
    SourceTypeBancontact
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    bic: typing.Optional[str] = pydantic.Field(alias="bic", default=None)
    iban_last4: typing.Optional[str] = pydantic.Field(alias="iban_last4", default=None)
    preferred_language: typing.Optional[str] = pydantic.Field(
        alias="preferred_language", default=None
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
