import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_au_becs_debit_display_preference import (
    PaymentMethodConfigurationCreateBodyAuBecsDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAuBecsDebitDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAuBecsDebit(typing_extensions.TypedDict):
    """
    Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAuBecsDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAuBecsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAuBecsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAuBecsDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
