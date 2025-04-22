import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_affirm_display_preference import (
    PaymentMethodConfigurationCreateBodyAffirmDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAffirmDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAffirm(typing_extensions.TypedDict):
    """
    [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAffirmDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAffirm(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAffirm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAffirmDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
