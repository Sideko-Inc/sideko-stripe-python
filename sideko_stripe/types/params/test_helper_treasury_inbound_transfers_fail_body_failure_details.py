import pydantic
import typing
import typing_extensions


class TestHelperTreasuryInboundTransfersFailBodyFailureDetails(
    typing_extensions.TypedDict
):
    """
    Details about a failed InboundTransfer.
    """

    code: typing_extensions.NotRequired[
        typing_extensions.Literal[
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
        ]
    ]


class _SerializerTestHelperTreasuryInboundTransfersFailBodyFailureDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryInboundTransfersFailBodyFailureDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    code: typing.Optional[
        typing_extensions.Literal[
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
        ]
    ] = pydantic.Field(alias="code", default=None)
