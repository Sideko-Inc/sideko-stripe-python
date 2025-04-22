import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_afterpay_clearpay_display_preference import (
    PaymentMethodConfigurationCreateBodyAfterpayClearpayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyAfterpayClearpayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyAfterpayClearpay(typing_extensions.TypedDict):
    """
    Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyAfterpayClearpayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyAfterpayClearpay(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationCreateBodyAfterpayClearpay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyAfterpayClearpayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
