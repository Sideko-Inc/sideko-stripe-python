import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_zip_display_preference import (
    PaymentMethodConfigurationUpdateBodyZipDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyZipDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyZip(typing_extensions.TypedDict):
    """
    Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyZipDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyZip(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyZip handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyZipDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
