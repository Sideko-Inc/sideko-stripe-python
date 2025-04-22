import pydantic
import typing
import typing_extensions

from .funding_instructions_bank_transfer_financial_address import (
    FundingInstructionsBankTransferFinancialAddress,
)


class PaymentIntentNextActionDisplayBankTransferInstructions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_remaining: typing.Optional[int] = pydantic.Field(
        alias="amount_remaining", default=None
    )
    """
    The remaining amount that needs to be transferred to complete the payment.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    financial_addresses: typing.Optional[
        typing.List[FundingInstructionsBankTransferFinancialAddress]
    ] = pydantic.Field(alias="financial_addresses", default=None)
    """
    A list of financial addresses that can be used to fund the customer balance
    """
    hosted_instructions_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_instructions_url", default=None
    )
    """
    A link to a hosted page that guides your customer through completing the transfer.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    A string identifying this payment. Instruct your customer to include this code in the reference or memo field of their bank transfer.
    """
    type_: typing_extensions.Literal[
        "eu_bank_transfer",
        "gb_bank_transfer",
        "jp_bank_transfer",
        "mx_bank_transfer",
        "us_bank_transfer",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of bank transfer
    """
