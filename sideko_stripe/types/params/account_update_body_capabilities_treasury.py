import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesTreasury(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesTreasury
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesTreasury(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesTreasury handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
