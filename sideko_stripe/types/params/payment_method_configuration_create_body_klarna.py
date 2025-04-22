import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_klarna_display_preference import (
    PaymentMethodConfigurationCreateBodyKlarnaDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyKlarnaDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyKlarna(typing_extensions.TypedDict):
    """
    Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyKlarnaDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyKlarna(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyKlarnaDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
