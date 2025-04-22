import pydantic
import typing
import typing_extensions

from .payment_method_options_customer_balance_eu_bank_account import (
    PaymentMethodOptionsCustomerBalanceEuBankAccount,
)


class PaymentMethodOptionsCustomerBalanceBankTransfer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        PaymentMethodOptionsCustomerBalanceEuBankAccount
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    requested_address_types: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "aba", "iban", "sepa", "sort_code", "spei", "swift", "zengin"
            ]
        ]
    ] = pydantic.Field(alias="requested_address_types", default=None)
    """
    List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.
    
    Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """
