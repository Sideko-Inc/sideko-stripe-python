import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsAlmaObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
