import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    """

    reference_prefix: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_prefix: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="reference_prefix", default=None
    )
