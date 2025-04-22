import pydantic
import typing
import typing_extensions

from .billing_meter_event_adjustment_create_body_cancel import (
    BillingMeterEventAdjustmentCreateBodyCancel,
    _SerializerBillingMeterEventAdjustmentCreateBodyCancel,
)


class BillingMeterEventAdjustmentCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingMeterEventAdjustmentCreateBody
    """

    cancel: typing_extensions.NotRequired[BillingMeterEventAdjustmentCreateBodyCancel]
    """
    Specifies which event to cancel.
    """

    event_name: typing_extensions.Required[str]
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["cancel"]]
    """
    Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
    """


class _SerializerBillingMeterEventAdjustmentCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingMeterEventAdjustmentCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cancel: typing.Optional[_SerializerBillingMeterEventAdjustmentCreateBodyCancel] = (
        pydantic.Field(alias="cancel", default=None)
    )
    event_name: str = pydantic.Field(
        alias="event_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    type_: typing_extensions.Literal["cancel"] = pydantic.Field(
        alias="type",
    )
