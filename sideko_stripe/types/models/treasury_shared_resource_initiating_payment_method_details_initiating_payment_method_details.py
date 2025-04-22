import pydantic
import typing
import typing_extensions

from .received_payment_method_details_financial_account import (
    ReceivedPaymentMethodDetailsFinancialAccount,
)
from .treasury_shared_resource_billing_details import (
    TreasurySharedResourceBillingDetails,
)
from .treasury_shared_resource_initiating_payment_method_details_us_bank_account import (
    TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccount,
)


class TreasurySharedResourceInitiatingPaymentMethodDetailsInitiatingPaymentMethodDetails(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    balance: typing.Optional[typing_extensions.Literal["payments"]] = pydantic.Field(
        alias="balance", default=None
    )
    """
    Set when `type` is `balance`.
    """
    billing_details: TreasurySharedResourceBillingDetails = pydantic.Field(
        alias="billing_details",
    )
    financial_account: typing.Optional[ReceivedPaymentMethodDetailsFinancialAccount] = (
        pydantic.Field(alias="financial_account", default=None)
    )
    issuing_card: typing.Optional[str] = pydantic.Field(
        alias="issuing_card", default=None
    )
    """
    Set when `type` is `issuing_card`. This is an [Issuing Card](https://stripe.com/docs/api#issuing_cards) ID.
    """
    type_: typing_extensions.Literal[
        "balance", "financial_account", "issuing_card", "stripe", "us_bank_account"
    ] = pydantic.Field(
        alias="type",
    )
    """
    Polymorphic type matching the originating money movement's source. This can be an external account, a Stripe balance, or a FinancialAccount.
    """
    us_bank_account: typing.Optional[
        TreasurySharedResourceInitiatingPaymentMethodDetailsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
