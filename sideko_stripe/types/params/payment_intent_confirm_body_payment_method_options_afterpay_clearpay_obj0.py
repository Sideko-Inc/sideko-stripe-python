import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]

    reference: typing_extensions.NotRequired[str]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsAfterpayClearpayObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
