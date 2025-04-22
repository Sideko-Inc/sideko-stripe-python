import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_intent_data_metadata import (
    CheckoutSessionCreateBodyPaymentIntentDataMetadata,
    _SerializerCheckoutSessionCreateBodyPaymentIntentDataMetadata,
)
from .checkout_session_create_body_payment_intent_data_shipping import (
    CheckoutSessionCreateBodyPaymentIntentDataShipping,
    _SerializerCheckoutSessionCreateBodyPaymentIntentDataShipping,
)
from .checkout_session_create_body_payment_intent_data_transfer_data import (
    CheckoutSessionCreateBodyPaymentIntentDataTransferData,
    _SerializerCheckoutSessionCreateBodyPaymentIntentDataTransferData,
)


class CheckoutSessionCreateBodyPaymentIntentData(typing_extensions.TypedDict):
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    application_fee_amount: typing_extensions.NotRequired[int]

    capture_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ]

    description: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentIntentDataMetadata
    ]

    on_behalf_of: typing_extensions.NotRequired[str]

    receipt_email: typing_extensions.NotRequired[str]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]

    shipping: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentIntentDataShipping
    ]

    statement_descriptor: typing_extensions.NotRequired[str]

    statement_descriptor_suffix: typing_extensions.NotRequired[str]

    transfer_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentIntentDataTransferData
    ]

    transfer_group: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentIntentData(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentIntentData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    metadata: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentIntentDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    shipping: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentIntentDataShipping
    ] = pydantic.Field(alias="shipping", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentIntentDataTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
