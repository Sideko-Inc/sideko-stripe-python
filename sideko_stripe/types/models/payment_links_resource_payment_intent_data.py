import pydantic
import typing
import typing_extensions

from .payment_links_resource_payment_intent_data_metadata import (
    PaymentLinksResourcePaymentIntentDataMetadata,
)


class PaymentLinksResourcePaymentIntentData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    """
    Indicates when the funds will be captured from the customer's account.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    metadata: PaymentLinksResourcePaymentIntentDataMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Payment Intents](https://stripe.com/docs/api/payment_intents) generated from this payment link.
    """
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    """
    Indicates that you intend to make future payments with the payment method collected during checkout.
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    For a non-card payment, information about the charge that appears on the customer's statement when this payment succeeds in creating a charge.
    """
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    """
    For a card payment, information about the charge that appears on the customer's statement when this payment succeeds in creating a charge. Concatenated with the account's statement descriptor prefix to form the complete statement descriptor.
    """
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
    """
    A string that identifies the resulting payment as part of a group. See the PaymentIntents [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
    """
