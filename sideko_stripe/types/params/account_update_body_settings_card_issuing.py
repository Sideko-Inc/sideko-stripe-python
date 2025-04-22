import pydantic
import typing
import typing_extensions

from .account_update_body_settings_card_issuing_tos_acceptance import (
    AccountUpdateBodySettingsCardIssuingTosAcceptance,
    _SerializerAccountUpdateBodySettingsCardIssuingTosAcceptance,
)


class AccountUpdateBodySettingsCardIssuing(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsCardIssuing
    """

    tos_acceptance: typing_extensions.NotRequired[
        AccountUpdateBodySettingsCardIssuingTosAcceptance
    ]


class _SerializerAccountUpdateBodySettingsCardIssuing(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[
        _SerializerAccountUpdateBodySettingsCardIssuingTosAcceptance
    ] = pydantic.Field(alias="tos_acceptance", default=None)
