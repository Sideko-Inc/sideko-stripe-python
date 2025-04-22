import pydantic
import typing
import typing_extensions


class BillingMeterEventAdjustmentCreateBodyCancel(typing_extensions.TypedDict):
    """
    Specifies which event to cancel.
    """

    identifier: typing_extensions.NotRequired[str]


class _SerializerBillingMeterEventAdjustmentCreateBodyCancel(pydantic.BaseModel):
    """
    Serializer for BillingMeterEventAdjustmentCreateBodyCancel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    identifier: typing.Optional[str] = pydantic.Field(alias="identifier", default=None)
