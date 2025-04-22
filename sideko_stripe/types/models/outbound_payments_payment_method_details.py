import pydantic
import typing
import typing_extensions

from .outbound_payments_payment_method_details_financial_account import (
    OutboundPaymentsPaymentMethodDetailsFinancialAccount,
)
from .treasury_shared_resource_billing_details import (
    TreasurySharedResourceBillingDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .outbound_payments_payment_method_details_us_bank_account import (
        OutboundPaymentsPaymentMethodDetailsUsBankAccount,
    )


class OutboundPaymentsPaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_details: TreasurySharedResourceBillingDetails = pydantic.Field(
        alias="billing_details",
    )
    financial_account: typing.Optional[
        OutboundPaymentsPaymentMethodDetailsFinancialAccount
    ] = pydantic.Field(alias="financial_account", default=None)
    type_: typing_extensions.Literal["financial_account", "us_bank_account"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of the payment method used in the OutboundPayment.
    """
    us_bank_account: typing.Optional[
        "OutboundPaymentsPaymentMethodDetailsUsBankAccount"
    ] = pydantic.Field(alias="us_bank_account", default=None)
