import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .billing_credit_balance_transaction import BillingCreditBalanceTransaction
    from .deleted_discount import DeletedDiscount
    from .discount import Discount


class InvoicesResourcePretaxCreditAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount, in cents (or local equivalent), of the pretax credit amount.
    """
    credit_balance_transaction: typing.Optional[
        typing.Union[str, "BillingCreditBalanceTransaction"]
    ] = pydantic.Field(alias="credit_balance_transaction", default=None)
    """
    The credit balance transaction that was applied to get this pretax credit amount.
    """
    discount: typing.Optional[typing.Union[str, "Discount", "DeletedDiscount"]] = (
        pydantic.Field(alias="discount", default=None)
    )
    """
    The discount that was applied to get this pretax credit amount.
    """
    type_: typing_extensions.Literal["credit_balance_transaction", "discount"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Type of the pretax credit amount referenced.
    """
