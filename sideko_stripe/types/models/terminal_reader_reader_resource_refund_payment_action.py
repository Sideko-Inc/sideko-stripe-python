import pydantic
import typing
import typing_extensions

from .terminal_reader_reader_resource_refund_payment_action_metadata import (
    TerminalReaderReaderResourceRefundPaymentActionMetadata,
)
from .terminal_reader_reader_resource_refund_payment_config import (
    TerminalReaderReaderResourceRefundPaymentConfig,
)

if typing_extensions.TYPE_CHECKING:
    from .charge import Charge
    from .payment_intent import PaymentIntent
    from .refund import Refund


class TerminalReaderReaderResourceRefundPaymentAction(pydantic.BaseModel):
    """
    Represents a reader action to refund a payment
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    """
    The amount being refunded.
    """
    charge: typing.Optional[typing.Union[str, "Charge"]] = pydantic.Field(
        alias="charge", default=None
    )
    """
    Charge that is being refunded.
    """
    metadata: typing.Optional[
        TerminalReaderReaderResourceRefundPaymentActionMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    Payment intent that is being refunded.
    """
    reason: typing.Optional[
        typing_extensions.Literal["duplicate", "fraudulent", "requested_by_customer"]
    ] = pydantic.Field(alias="reason", default=None)
    """
    The reason for the refund.
    """
    refund: typing.Optional[typing.Union[str, "Refund"]] = pydantic.Field(
        alias="refund", default=None
    )
    """
    Unique identifier for the refund object.
    """
    refund_application_fee: typing.Optional[bool] = pydantic.Field(
        alias="refund_application_fee", default=None
    )
    """
    Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    """
    refund_payment_config: typing.Optional[
        TerminalReaderReaderResourceRefundPaymentConfig
    ] = pydantic.Field(alias="refund_payment_config", default=None)
    """
    Represents a per-transaction override of a reader configuration
    """
    reverse_transfer: typing.Optional[bool] = pydantic.Field(
        alias="reverse_transfer", default=None
    )
    """
    Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
    """
