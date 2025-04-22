import pydantic
import typing
import typing_extensions


class LinkAccountSessionCreateBodyAccountHolder(typing_extensions.TypedDict):
    """
    The account holder to link accounts for.
    """

    account: typing_extensions.NotRequired[str]

    customer: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "customer"]]


class _SerializerLinkAccountSessionCreateBodyAccountHolder(pydantic.BaseModel):
    """
    Serializer for LinkAccountSessionCreateBodyAccountHolder handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    type_: typing_extensions.Literal["account", "customer"] = pydantic.Field(
        alias="type",
    )
