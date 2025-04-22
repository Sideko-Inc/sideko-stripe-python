import pydantic
import typing
import typing_extensions


class AccountCreateBodySettingsBranding(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsBranding
    """

    icon: typing_extensions.NotRequired[str]

    logo: typing_extensions.NotRequired[str]

    primary_color: typing_extensions.NotRequired[str]

    secondary_color: typing_extensions.NotRequired[str]


class _SerializerAccountCreateBodySettingsBranding(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsBranding handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    icon: typing.Optional[str] = pydantic.Field(alias="icon", default=None)
    logo: typing.Optional[str] = pydantic.Field(alias="logo", default=None)
    primary_color: typing.Optional[str] = pydantic.Field(
        alias="primary_color", default=None
    )
    secondary_color: typing.Optional[str] = pydantic.Field(
        alias="secondary_color", default=None
    )
