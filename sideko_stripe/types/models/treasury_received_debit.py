import pydantic
import typing
import typing_extensions

from .treasury_received_debits_resource_linked_flows import (
    TreasuryReceivedDebitsResourceLinkedFlows,
)
from .treasury_received_debits_resource_reversal_details import (
    TreasuryReceivedDebitsResourceReversalDetails,
)
from .treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details import (
    TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .treasury_transaction import TreasuryTransaction


class TreasuryReceivedDebit(pydantic.BaseModel):
    """
    ReceivedDebits represent funds pulled from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts). These are not initiated from the FinancialAccount.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount (in cents) transferred.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: str = pydantic.Field(
        alias="description",
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    failure_code: typing.Optional[
        typing_extensions.Literal[
            "account_closed",
            "account_frozen",
            "insufficient_funds",
            "international_transaction",
            "other",
        ]
    ] = pydantic.Field(alias="failure_code", default=None)
    """
    Reason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn't have sufficient funds, is closed, or is frozen.
    """
    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    """
    The FinancialAccount that funds were pulled from.
    """
    hosted_regulatory_receipt_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_regulatory_receipt_url", default=None
    )
    """
    A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    initiating_payment_method_details: typing.Optional[
        TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails
    ] = pydantic.Field(alias="initiating_payment_method_details", default=None)
    linked_flows: TreasuryReceivedDebitsResourceLinkedFlows = pydantic.Field(
        alias="linked_flows",
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: typing_extensions.Literal["ach", "card", "stripe"] = pydantic.Field(
        alias="network",
    )
    """
    The network used for the ReceivedDebit.
    """
    object: typing_extensions.Literal["treasury.received_debit"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reversal_details: typing.Optional[TreasuryReceivedDebitsResourceReversalDetails] = (
        pydantic.Field(alias="reversal_details", default=None)
    )
    status: typing_extensions.Literal["failed", "succeeded"] = pydantic.Field(
        alias="status",
    )
    """
    Status of the ReceivedDebit. ReceivedDebits are created with a status of either `succeeded` (approved) or `failed` (declined). The failure reason can be found under the `failure_code`.
    """
    transaction: typing.Optional[typing.Union[str, "TreasuryTransaction"]] = (
        pydantic.Field(alias="transaction", default=None)
    )
    """
    The Transaction associated with this object.
    """
