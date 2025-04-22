import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_automatic_tax_liability import (
    SubscriptionScheduleCreateBodyPhasesItemAutomaticTaxLiability,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemAutomaticTaxLiability,
)


class SubscriptionScheduleCreateBodyPhasesItemAutomaticTax(typing_extensions.TypedDict):
    """
    SubscriptionScheduleCreateBodyPhasesItemAutomaticTax
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemAutomaticTaxLiability
    ]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemAutomaticTax(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
