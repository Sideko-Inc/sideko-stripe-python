import pydantic
import typing
import typing_extensions

from .account_create_body_settings_treasury_tos_acceptance import (
    AccountCreateBodySettingsTreasuryTosAcceptance,
    _SerializerAccountCreateBodySettingsTreasuryTosAcceptance,
)


class AccountCreateBodySettingsTreasury(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsTreasury
    """

    tos_acceptance: typing_extensions.NotRequired[
        AccountCreateBodySettingsTreasuryTosAcceptance
    ]


class _SerializerAccountCreateBodySettingsTreasury(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsTreasury handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[
        _SerializerAccountCreateBodySettingsTreasuryTosAcceptance
    ] = pydantic.Field(alias="tos_acceptance", default=None)
