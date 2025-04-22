import pydantic
import typing
import typing_extensions

from .source_transaction_ach_credit_transfer_data import (
    SourceTransactionAchCreditTransferData,
)
from .source_transaction_chf_credit_transfer_data import (
    SourceTransactionChfCreditTransferData,
)
from .source_transaction_gbp_credit_transfer_data import (
    SourceTransactionGbpCreditTransferData,
)
from .source_transaction_paper_check_data import SourceTransactionPaperCheckData
from .source_transaction_sepa_credit_transfer_data import (
    SourceTransactionSepaCreditTransferData,
)


class SourceTransaction(pydantic.BaseModel):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach_credit_transfer: typing.Optional[SourceTransactionAchCreditTransferData] = (
        pydantic.Field(alias="ach_credit_transfer", default=None)
    )
    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the amount your customer has pushed to the receiver.
    """
    chf_credit_transfer: typing.Optional[SourceTransactionChfCreditTransferData] = (
        pydantic.Field(alias="chf_credit_transfer", default=None)
    )
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
    gbp_credit_transfer: typing.Optional[SourceTransactionGbpCreditTransferData] = (
        pydantic.Field(alias="gbp_credit_transfer", default=None)
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["source_transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    paper_check: typing.Optional[SourceTransactionPaperCheckData] = pydantic.Field(
        alias="paper_check", default=None
    )
    sepa_credit_transfer: typing.Optional[SourceTransactionSepaCreditTransferData] = (
        pydantic.Field(alias="sepa_credit_transfer", default=None)
    )
    source: str = pydantic.Field(
        alias="source",
    )
    """
    The ID of the source this transaction is attached to.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the transaction, one of `succeeded`, `pending`, or `failed`.
    """
    type_: typing_extensions.Literal[
        "ach_credit_transfer",
        "ach_debit",
        "alipay",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of source this transaction is attached to.
    """
