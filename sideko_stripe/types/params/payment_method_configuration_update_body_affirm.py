import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_affirm_display_preference import (
    PaymentMethodConfigurationUpdateBodyAffirmDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyAffirmDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyAffirm(typing_extensions.TypedDict):
    """
    [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAffirmDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyAffirm(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyAffirm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAffirmDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
