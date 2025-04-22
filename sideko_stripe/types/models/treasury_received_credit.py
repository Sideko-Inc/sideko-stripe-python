import pydantic
import typing
import typing_extensions

from .treasury_received_credits_resource_reversal_details import (
    TreasuryReceivedCreditsResourceReversalDetails,
)
from .treasury_shared_resource_initiating_payment_method_details_initiating_payment_method_details import (
    TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .treasury_received_credits_resource_linked_flows import (
        TreasuryReceivedCreditsResourceLinkedFlows,
    )
    from .treasury_transaction import TreasuryTransaction


class TreasuryReceivedCredit(pydantic.BaseModel):
    """
    ReceivedCredits represent funds sent to a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.
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
            "account_closed", "account_frozen", "international_transaction", "other"
        ]
    ] = pydantic.Field(alias="failure_code", default=None)
    """
    Reason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.
    """
    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    """
    The FinancialAccount that received the funds.
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
    initiating_payment_method_details: TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails = pydantic.Field(
        alias="initiating_payment_method_details",
    )
    linked_flows: "TreasuryReceivedCreditsResourceLinkedFlows" = pydantic.Field(
        alias="linked_flows",
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: typing_extensions.Literal["ach", "card", "stripe", "us_domestic_wire"] = (
        pydantic.Field(
            alias="network",
        )
    )
    """
    The rails used to send the funds.
    """
    object: typing_extensions.Literal["treasury.received_credit"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reversal_details: typing.Optional[
        TreasuryReceivedCreditsResourceReversalDetails
    ] = pydantic.Field(alias="reversal_details", default=None)
    status: typing_extensions.Literal["failed", "succeeded"] = pydantic.Field(
        alias="status",
    )
    """
    Status of the ReceivedCredit. ReceivedCredits are created either `succeeded` (approved) or `failed` (declined). If a ReceivedCredit is declined, the failure reason can be found in the `failure_code` field.
    """
    transaction: typing.Optional[typing.Union[str, "TreasuryTransaction"]] = (
        pydantic.Field(alias="transaction", default=None)
    )
    """
    The Transaction associated with this object.
    """
