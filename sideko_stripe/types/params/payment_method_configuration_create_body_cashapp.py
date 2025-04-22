import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_cashapp_display_preference import (
    PaymentMethodConfigurationCreateBodyCashappDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyCashappDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyCashapp(typing_extensions.TypedDict):
    """
    Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyCashappDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyCashapp(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyCashapp handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyCashappDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
