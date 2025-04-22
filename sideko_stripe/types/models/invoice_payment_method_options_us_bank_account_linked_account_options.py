import pydantic
import typing
import typing_extensions

from .invoice_payment_method_options_us_bank_account_linked_account_options_filters import (
    InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptionsFilters,
)


class InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    filters: typing.Optional[
        InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptionsFilters
    ] = pydantic.Field(alias="filters", default=None)
    permissions: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ] = pydantic.Field(alias="permissions", default=None)
    """
    The list of permissions to request. The `payment_method` permission must be included.
    """
    prefetch: typing.Optional[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ] = pydantic.Field(alias="prefetch", default=None)
    """
    Data features requested to be retrieved upon account creation.
    """
