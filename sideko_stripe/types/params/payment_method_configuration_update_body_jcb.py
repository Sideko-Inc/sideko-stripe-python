import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_jcb_display_preference import (
    PaymentMethodConfigurationUpdateBodyJcbDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyJcbDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyJcb(typing_extensions.TypedDict):
    """
    JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyJcbDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyJcb(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyJcb handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyJcbDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
