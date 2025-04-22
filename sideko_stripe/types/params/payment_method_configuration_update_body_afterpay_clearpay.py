import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_afterpay_clearpay_display_preference import (
    PaymentMethodConfigurationUpdateBodyAfterpayClearpayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyAfterpayClearpayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyAfterpayClearpay(typing_extensions.TypedDict):
    """
    Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyAfterpayClearpayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyAfterpayClearpay(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyAfterpayClearpay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyAfterpayClearpayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
