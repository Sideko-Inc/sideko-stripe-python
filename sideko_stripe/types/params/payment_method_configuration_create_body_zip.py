import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_zip_display_preference import (
    PaymentMethodConfigurationCreateBodyZipDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyZipDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyZip(typing_extensions.TypedDict):
    """
    Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyZipDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyZip(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyZip handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyZipDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
