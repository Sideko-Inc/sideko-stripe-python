import pydantic
import typing
import typing_extensions


class PaymentMethodUsBankAccountBlocked(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    network_code: typing.Optional[
        typing_extensions.Literal[
            "R02",
            "R03",
            "R04",
            "R05",
            "R07",
            "R08",
            "R10",
            "R11",
            "R16",
            "R20",
            "R29",
            "R31",
        ]
    ] = pydantic.Field(alias="network_code", default=None)
    """
    The ACH network code that resulted in this block.
    """
    reason: typing.Optional[
        typing_extensions.Literal[
            "bank_account_closed",
            "bank_account_frozen",
            "bank_account_invalid_details",
            "bank_account_restricted",
            "bank_account_unusable",
            "debit_not_authorized",
        ]
    ] = pydantic.Field(alias="reason", default=None)
    """
    The reason why this PaymentMethod's fingerprint has been blocked
    """
