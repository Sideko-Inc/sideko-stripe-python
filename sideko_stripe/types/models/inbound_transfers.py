import pydantic
import typing
import typing_extensions

from .treasury_shared_resource_billing_details import (
    TreasurySharedResourceBillingDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .inbound_transfers_payment_method_details_us_bank_account import (
        InboundTransfersPaymentMethodDetailsUsBankAccount,
    )


class InboundTransfers(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_details: TreasurySharedResourceBillingDetails = pydantic.Field(
        alias="billing_details",
    )
    type_: typing_extensions.Literal["us_bank_account"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the payment method used in the InboundTransfer.
    """
    us_bank_account: typing.Optional[
        "InboundTransfersPaymentMethodDetailsUsBankAccount"
    ] = pydantic.Field(alias="us_bank_account", default=None)
