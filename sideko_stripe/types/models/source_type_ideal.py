import pydantic
import typing


class SourceTypeIdeal(pydantic.BaseModel):
    """
    SourceTypeIdeal
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank: typing.Optional[str] = pydantic.Field(alias="bank", default=None)
    bic: typing.Optional[str] = pydantic.Field(alias="bic", default=None)
    iban_last4: typing.Optional[str] = pydantic.Field(alias="iban_last4", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
