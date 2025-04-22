import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_mandate_data_obj0 import (
    SetupIntentConfirmBodyMandateDataObj0,
    _SerializerSetupIntentConfirmBodyMandateDataObj0,
)
from .setup_intent_confirm_body_mandate_data_obj2 import (
    SetupIntentConfirmBodyMandateDataObj2,
    _SerializerSetupIntentConfirmBodyMandateDataObj2,
)
from .setup_intent_confirm_body_payment_method_data import (
    SetupIntentConfirmBodyPaymentMethodData,
    _SerializerSetupIntentConfirmBodyPaymentMethodData,
)
from .setup_intent_confirm_body_payment_method_options import (
    SetupIntentConfirmBodyPaymentMethodOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptions,
)


class SetupIntentConfirmBody(typing_extensions.TypedDict, total=False):
    """
    SetupIntentConfirmBody
    """

    client_secret: typing_extensions.NotRequired[str]
    """
    The client secret of the SetupIntent.
    """

    confirmation_token: typing_extensions.NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this SetupIntent.
    
    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    mandate_data: typing_extensions.NotRequired[
        typing.Union[
            SetupIntentConfirmBodyMandateDataObj0,
            str,
            SetupIntentConfirmBodyMandateDataObj2,
        ]
    ]

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodData
    ]
    """
    When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
    value in the SetupIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this SetupIntent.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate on the payment method's app or site.
    If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
    This parameter is only used for cards and other redirect-based payment methods.
    """

    use_stripe_sdk: typing_extensions.NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """


class _SerializerSetupIntentConfirmBody(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    confirmation_token: typing.Optional[str] = pydantic.Field(
        alias="confirmation_token", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    mandate_data: typing.Optional[
        typing.Union[
            _SerializerSetupIntentConfirmBodyMandateDataObj0,
            str,
            _SerializerSetupIntentConfirmBodyMandateDataObj2,
        ]
    ] = pydantic.Field(alias="mandate_data", default=None)
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    use_stripe_sdk: typing.Optional[bool] = pydantic.Field(
        alias="use_stripe_sdk", default=None
    )
