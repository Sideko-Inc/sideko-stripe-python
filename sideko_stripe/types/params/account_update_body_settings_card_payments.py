import pydantic
import typing
import typing_extensions

from .account_update_body_settings_card_payments_decline_on import (
    AccountUpdateBodySettingsCardPaymentsDeclineOn,
    _SerializerAccountUpdateBodySettingsCardPaymentsDeclineOn,
)


class AccountUpdateBodySettingsCardPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsCardPayments
    """

    decline_on: typing_extensions.NotRequired[
        AccountUpdateBodySettingsCardPaymentsDeclineOn
    ]

    statement_descriptor_prefix: typing_extensions.NotRequired[str]

    statement_descriptor_prefix_kana: typing_extensions.NotRequired[
        typing.Union[str, str]
    ]

    statement_descriptor_prefix_kanji: typing_extensions.NotRequired[
        typing.Union[str, str]
    ]


class _SerializerAccountUpdateBodySettingsCardPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsCardPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    decline_on: typing.Optional[
        _SerializerAccountUpdateBodySettingsCardPaymentsDeclineOn
    ] = pydantic.Field(alias="decline_on", default=None)
    statement_descriptor_prefix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_prefix", default=None
    )
    statement_descriptor_prefix_kana: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="statement_descriptor_prefix_kana", default=None)
    )
    statement_descriptor_prefix_kanji: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="statement_descriptor_prefix_kanji", default=None)
    )
