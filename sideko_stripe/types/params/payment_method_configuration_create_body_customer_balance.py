import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_customer_balance_display_preference import (
    PaymentMethodConfigurationCreateBodyCustomerBalanceDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyCustomerBalanceDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyCustomerBalance(typing_extensions.TypedDict):
    """
    Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyCustomerBalanceDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyCustomerBalance(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationCreateBodyCustomerBalance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyCustomerBalanceDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
