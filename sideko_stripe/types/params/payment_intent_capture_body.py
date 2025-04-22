import pydantic
import typing
import typing_extensions

from .payment_intent_capture_body_metadata_obj0 import (
    PaymentIntentCaptureBodyMetadataObj0,
    _SerializerPaymentIntentCaptureBodyMetadataObj0,
)
from .payment_intent_capture_body_transfer_data import (
    PaymentIntentCaptureBodyTransferData,
    _SerializerPaymentIntentCaptureBodyTransferData,
)


class PaymentIntentCaptureBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentCaptureBody
    """

    amount_to_capture: typing_extensions.NotRequired[int]
    """
    The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it's not provided.
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    final_capture: typing_extensions.NotRequired[bool]
    """
    Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they're captured in future requests. You can only use this setting when [multicapture](https://stripe.com/docs/payments/multicapture) is available for PaymentIntents.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCaptureBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    
    Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    """

    statement_descriptor_suffix: typing_extensions.NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    """

    transfer_data: typing_extensions.NotRequired[PaymentIntentCaptureBodyTransferData]
    """
    The parameters that you can use to automatically create a transfer after the payment
    is captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """


class _SerializerPaymentIntentCaptureBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCaptureBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount_to_capture: typing.Optional[int] = pydantic.Field(
        alias="amount_to_capture", default=None
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    final_capture: typing.Optional[bool] = pydantic.Field(
        alias="final_capture", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPaymentIntentCaptureBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[_SerializerPaymentIntentCaptureBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
