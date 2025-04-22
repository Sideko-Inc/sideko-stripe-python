import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    """

    reference_prefix: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_prefix: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="reference_prefix", default=None
    )
