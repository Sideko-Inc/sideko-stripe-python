import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_customer_balance_display_preference import (
    PaymentMethodConfigurationUpdateBodyCustomerBalanceDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyCustomerBalanceDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyCustomerBalance(typing_extensions.TypedDict):
    """
    Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyCustomerBalanceDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyCustomerBalance(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyCustomerBalance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyCustomerBalanceDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
