import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_multibanco_display_preference import (
    PaymentMethodConfigurationUpdateBodyMultibancoDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyMultibancoDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyMultibanco(typing_extensions.TypedDict):
    """
    Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyMultibancoDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyMultibanco(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyMultibanco handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyMultibancoDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
