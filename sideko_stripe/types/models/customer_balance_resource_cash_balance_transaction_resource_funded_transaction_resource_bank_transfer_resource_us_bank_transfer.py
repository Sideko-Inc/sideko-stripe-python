import pydantic
import typing
import typing_extensions


class CustomerBalanceResourceCashBalanceTransactionResourceFundedTransactionResourceBankTransferResourceUsBankTransfer(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    network: typing.Optional[
        typing_extensions.Literal["ach", "domestic_wire_us", "swift"]
    ] = pydantic.Field(alias="network", default=None)
    """
    The banking network used for this funding.
    """
    sender_name: typing.Optional[str] = pydantic.Field(
        alias="sender_name", default=None
    )
    """
    The full name of the sender, as supplied by the sending bank.
    """
