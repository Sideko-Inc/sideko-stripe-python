import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsNzBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
