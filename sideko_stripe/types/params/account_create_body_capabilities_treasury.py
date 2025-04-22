import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesTreasury(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesTreasury
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesTreasury(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesTreasury handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
