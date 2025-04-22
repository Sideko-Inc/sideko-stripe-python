import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_default_settings_automatic_tax_liability import (
    SubscriptionScheduleCreateBodyDefaultSettingsAutomaticTaxLiability,
    _SerializerSubscriptionScheduleCreateBodyDefaultSettingsAutomaticTaxLiability,
)


class SubscriptionScheduleCreateBodyDefaultSettingsAutomaticTax(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyDefaultSettingsAutomaticTax
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyDefaultSettingsAutomaticTaxLiability
    ]


class _SerializerSubscriptionScheduleCreateBodyDefaultSettingsAutomaticTax(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyDefaultSettingsAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyDefaultSettingsAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
