import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0MandateOptions
    """

    custom_mandate_url: typing_extensions.NotRequired[typing.Union[str, str]]

    interval_description: typing_extensions.NotRequired[str]

    payment_schedule: typing_extensions.NotRequired[
        typing_extensions.Literal["combined", "interval", "sporadic"]
    ]

    transaction_type: typing_extensions.NotRequired[
        typing_extensions.Literal["business", "personal"]
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsAcssDebitObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_mandate_url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="custom_mandate_url", default=None
    )
    interval_description: typing.Optional[str] = pydantic.Field(
        alias="interval_description", default=None
    )
    payment_schedule: typing.Optional[
        typing_extensions.Literal["combined", "interval", "sporadic"]
    ] = pydantic.Field(alias="payment_schedule", default=None)
    transaction_type: typing.Optional[
        typing_extensions.Literal["business", "personal"]
    ] = pydantic.Field(alias="transaction_type", default=None)
