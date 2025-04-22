import pydantic
import typing


class SourceTypeWechat(pydantic.BaseModel):
    """
    SourceTypeWechat
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    prepay_id: typing.Optional[str] = pydantic.Field(alias="prepay_id", default=None)
    qr_code_url: typing.Optional[str] = pydantic.Field(
        alias="qr_code_url", default=None
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
