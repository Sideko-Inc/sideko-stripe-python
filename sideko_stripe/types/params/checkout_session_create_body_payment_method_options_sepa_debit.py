import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_sepa_debit_mandate_options import (
    CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebitMandateOptions,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSepaDebitMandateOptions,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit
    """

    mandate_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
