import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_jcb_display_preference import (
    PaymentMethodConfigurationCreateBodyJcbDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyJcbDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyJcb(typing_extensions.TypedDict):
    """
    JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyJcbDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyJcb(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyJcb handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyJcbDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
