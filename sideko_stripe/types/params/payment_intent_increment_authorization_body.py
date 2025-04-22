import pydantic
import typing
import typing_extensions

from .payment_intent_increment_authorization_body_metadata import (
    PaymentIntentIncrementAuthorizationBodyMetadata,
    _SerializerPaymentIntentIncrementAuthorizationBodyMetadata,
)
from .payment_intent_increment_authorization_body_transfer_data import (
    PaymentIntentIncrementAuthorizationBodyTransferData,
    _SerializerPaymentIntentIncrementAuthorizationBodyTransferData,
)


class PaymentIntentIncrementAuthorizationBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentIncrementAuthorizationBody
    """

    amount: typing_extensions.Required[int]
    """
    The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        PaymentIntentIncrementAuthorizationBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """

    transfer_data: typing_extensions.NotRequired[
        PaymentIntentIncrementAuthorizationBodyTransferData
    ]
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """


class _SerializerPaymentIntentIncrementAuthorizationBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentIncrementAuthorizationBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        _SerializerPaymentIntentIncrementAuthorizationBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    transfer_data: typing.Optional[
        _SerializerPaymentIntentIncrementAuthorizationBodyTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
