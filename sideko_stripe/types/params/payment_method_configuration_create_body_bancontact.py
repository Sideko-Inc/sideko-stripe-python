import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_bancontact_display_preference import (
    PaymentMethodConfigurationCreateBodyBancontactDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyBancontactDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyBancontact(typing_extensions.TypedDict):
    """
    Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyBancontactDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyBancontact(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyBancontact handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyBancontactDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
