import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions
    """

    reference_prefix: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_prefix: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="reference_prefix", default=None
    )
