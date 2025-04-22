import pydantic
import typing
import typing_extensions


class TestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails(
    typing_extensions.TypedDict
):
    """
    Details about a returned OutboundTransfer.
    """

    code: typing_extensions.NotRequired[
        typing_extensions.Literal[
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
        ]
    ]


class _SerializerTestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails handling case conversions
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
            "declined",
            "incorrect_account_holder_name",
            "invalid_account_number",
            "invalid_currency",
            "no_account",
            "other",
        ]
    ] = pydantic.Field(alias="code", default=None)
