import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .refund import Refund


class CustomerBalanceResourceCashBalanceTransactionResourceRefundedFromPaymentTransaction(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    refund: typing.Union[str, "Refund"] = pydantic.Field(
        alias="refund",
    )
    """
    The [Refund](https://stripe.com/docs/api/refunds/object) that moved these funds into the customer's cash balance.
    """
