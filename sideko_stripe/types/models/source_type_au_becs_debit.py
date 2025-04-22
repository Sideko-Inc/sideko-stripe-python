import pydantic
import typing


class SourceTypeAuBecsDebit(pydantic.BaseModel):
    """
    SourceTypeAuBecsDebit
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bsb_number: typing.Optional[str] = pydantic.Field(alias="bsb_number", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
