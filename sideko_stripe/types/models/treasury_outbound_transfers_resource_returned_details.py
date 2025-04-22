import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .treasury_transaction import TreasuryTransaction


class TreasuryOutboundTransfersResourceReturnedDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing_extensions.Literal[
        "account_closed",
        "account_frozen",
        "bank_account_restricted",
        "bank_ownership_changed",
        "declined",
        "incorrect_account_holder_name",
        "invalid_account_number",
        "invalid_currency",
        "no_account",
        "other",
    ] = pydantic.Field(
        alias="code",
    )
    """
    Reason for the return.
    """
    transaction: typing.Union[str, "TreasuryTransaction"] = pydantic.Field(
        alias="transaction",
    )
    """
    The Transaction associated with this object.
    """
