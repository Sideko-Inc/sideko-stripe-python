import pydantic
import typing
import typing_extensions


class TaxIdListOwner(typing_extensions.TypedDict):
    """
    The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.
    """

    account: typing_extensions.NotRequired[str]

    customer: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[
        typing_extensions.Literal["account", "application", "customer", "self"]
    ]


class _SerializerTaxIdListOwner(pydantic.BaseModel):
    """
    Serializer for TaxIdListOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    type_: typing_extensions.Literal["account", "application", "customer", "self"] = (
        pydantic.Field(
            alias="type",
        )
    )
