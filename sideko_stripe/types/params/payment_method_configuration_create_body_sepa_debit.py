import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_sepa_debit_display_preference import (
    PaymentMethodConfigurationCreateBodySepaDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodySepaDebitDisplayPreference,
)


class PaymentMethodConfigurationCreateBodySepaDebit(typing_extensions.TypedDict):
    """
    The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodySepaDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodySepaDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodySepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodySepaDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
