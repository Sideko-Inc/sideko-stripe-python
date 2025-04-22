import pydantic
import typing
import typing_extensions

from .account_create_body_settings_card_issuing_tos_acceptance import (
    AccountCreateBodySettingsCardIssuingTosAcceptance,
    _SerializerAccountCreateBodySettingsCardIssuingTosAcceptance,
)


class AccountCreateBodySettingsCardIssuing(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsCardIssuing
    """

    tos_acceptance: typing_extensions.NotRequired[
        AccountCreateBodySettingsCardIssuingTosAcceptance
    ]


class _SerializerAccountCreateBodySettingsCardIssuing(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[
        _SerializerAccountCreateBodySettingsCardIssuingTosAcceptance
    ] = pydantic.Field(alias="tos_acceptance", default=None)
