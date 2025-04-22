import pydantic
import typing


class SourceTypeAlipay(pydantic.BaseModel):
    """
    SourceTypeAlipay
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data_string: typing.Optional[str] = pydantic.Field(
        alias="data_string", default=None
    )
    native_url: typing.Optional[str] = pydantic.Field(alias="native_url", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
