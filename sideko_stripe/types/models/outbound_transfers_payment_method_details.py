import pydantic
import typing
import typing_extensions

from .outbound_transfers_payment_method_details_financial_account import (
    OutboundTransfersPaymentMethodDetailsFinancialAccount,
)
from .treasury_shared_resource_billing_details import (
    TreasurySharedResourceBillingDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .outbound_transfers_payment_method_details_us_bank_account import (
        OutboundTransfersPaymentMethodDetailsUsBankAccount,
    )


class OutboundTransfersPaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_details: TreasurySharedResourceBillingDetails = pydantic.Field(
        alias="billing_details",
    )
    financial_account: typing.Optional[
        OutboundTransfersPaymentMethodDetailsFinancialAccount
    ] = pydantic.Field(alias="financial_account", default=None)
    type_: typing_extensions.Literal["financial_account", "us_bank_account"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of the payment method used in the OutboundTransfer.
    """
    us_bank_account: typing.Optional[
        "OutboundTransfersPaymentMethodDetailsUsBankAccount"
    ] = pydantic.Field(alias="us_bank_account", default=None)
