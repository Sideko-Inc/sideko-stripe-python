import pydantic
import typing


class SourceTypeGiropay(pydantic.BaseModel):
    """
    SourceTypeGiropay
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    bic: typing.Optional[str] = pydantic.Field(alias="bic", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
