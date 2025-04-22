import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_default_settings_automatic_tax_liability import (
    SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTaxLiability,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTaxLiability,
)


class SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTaxLiability
    ]


class _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
