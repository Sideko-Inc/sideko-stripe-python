import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0
    """

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsTwintObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
