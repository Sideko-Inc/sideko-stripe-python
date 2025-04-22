import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_cashapp_display_preference import (
    PaymentMethodConfigurationUpdateBodyCashappDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyCashappDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyCashapp(typing_extensions.TypedDict):
    """
    Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyCashappDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyCashapp(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyCashapp handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyCashappDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
