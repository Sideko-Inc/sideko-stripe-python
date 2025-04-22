import pydantic
import typing
import typing_extensions

from .account_update_body_settings_treasury_tos_acceptance import (
    AccountUpdateBodySettingsTreasuryTosAcceptance,
    _SerializerAccountUpdateBodySettingsTreasuryTosAcceptance,
)


class AccountUpdateBodySettingsTreasury(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsTreasury
    """

    tos_acceptance: typing_extensions.NotRequired[
        AccountUpdateBodySettingsTreasuryTosAcceptance
    ]


class _SerializerAccountUpdateBodySettingsTreasury(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsTreasury handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[
        _SerializerAccountUpdateBodySettingsTreasuryTosAcceptance
    ] = pydantic.Field(alias="tos_acceptance", default=None)
