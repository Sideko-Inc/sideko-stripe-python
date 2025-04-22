import pydantic
import typing_extensions


class TreasuryInboundTransfersResourceFailureDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing_extensions.Literal[
        "account_closed",
        "account_frozen",
        "bank_account_restricted",
        "bank_ownership_changed",
        "debit_not_authorized",
        "incorrect_account_holder_address",
        "incorrect_account_holder_name",
        "incorrect_account_holder_tax_id",
        "insufficient_funds",
        "invalid_account_number",
        "invalid_currency",
        "no_account",
        "other",
    ] = pydantic.Field(
        alias="code",
    )
    """
    Reason for the failure.
    """
