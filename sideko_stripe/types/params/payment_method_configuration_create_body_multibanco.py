import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_multibanco_display_preference import (
    PaymentMethodConfigurationCreateBodyMultibancoDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyMultibancoDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyMultibanco(typing_extensions.TypedDict):
    """
    Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyMultibancoDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyMultibanco(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyMultibanco handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyMultibancoDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
