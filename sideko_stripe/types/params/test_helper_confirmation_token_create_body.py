import pydantic
import typing
import typing_extensions

from .test_helper_confirmation_token_create_body_payment_method_data import (
    TestHelperConfirmationTokenCreateBodyPaymentMethodData,
    _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodData,
)
from .test_helper_confirmation_token_create_body_shipping import (
    TestHelperConfirmationTokenCreateBodyShipping,
    _SerializerTestHelperConfirmationTokenCreateBodyShipping,
)


class TestHelperConfirmationTokenCreateBody(typing_extensions.TypedDict, total=False):
    """
    TestHelperConfirmationTokenCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of an existing PaymentMethod.
    """

    payment_method_data: typing_extensions.NotRequired[
        TestHelperConfirmationTokenCreateBodyPaymentMethodData
    ]
    """
    If provided, this hash will be used to create a PaymentMethod.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    Return URL used to confirm the Intent.
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]
    """
    Indicates that you intend to make future payments with this ConfirmationToken's payment method.
    
    The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
    """

    shipping: typing_extensions.NotRequired[
        TestHelperConfirmationTokenCreateBodyShipping
    ]
    """
    Shipping information for this ConfirmationToken.
    """


class _SerializerTestHelperConfirmationTokenCreateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperConfirmationTokenCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    shipping: typing.Optional[
        _SerializerTestHelperConfirmationTokenCreateBodyShipping
    ] = pydantic.Field(alias="shipping", default=None)
