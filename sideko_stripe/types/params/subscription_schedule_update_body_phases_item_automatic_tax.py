import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_phases_item_automatic_tax_liability import (
    SubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability,
)


class SubscriptionScheduleUpdateBodyPhasesItemAutomaticTax(typing_extensions.TypedDict):
    """
    SubscriptionScheduleUpdateBodyPhasesItemAutomaticTax
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability
    ]


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemAutomaticTax(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
