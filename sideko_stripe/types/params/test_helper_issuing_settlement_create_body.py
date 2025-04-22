import pydantic
import typing
import typing_extensions


class TestHelperIssuingSettlementCreateBody(typing_extensions.TypedDict, total=False):
    """
    TestHelperIssuingSettlementCreateBody
    """

    bin: typing_extensions.Required[str]
    """
    The Bank Identification Number reflecting this settlement record.
    """

    clearing_date: typing_extensions.Required[int]
    """
    The date that the transactions are cleared and posted to user's accounts.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    interchange_fees_amount: typing_extensions.NotRequired[int]
    """
    The total interchange received as reimbursement for the transactions.
    """

    net_total_amount: typing_extensions.Required[int]
    """
    The total net amount required to settle with the network.
    """

    network: typing_extensions.NotRequired[typing_extensions.Literal["maestro", "visa"]]
    """
    The card network for this settlement. One of ["visa", "maestro"]
    """

    network_settlement_identifier: typing_extensions.NotRequired[str]
    """
    The Settlement Identification Number assigned by the network.
    """

    transaction_amount: typing_extensions.NotRequired[int]
    """
    The total transaction amount reflected in this settlement.
    """

    transaction_count: typing_extensions.NotRequired[int]
    """
    The total number of transactions reflected in this settlement.
    """


class _SerializerTestHelperIssuingSettlementCreateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingSettlementCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    bin: str = pydantic.Field(
        alias="bin",
    )
    clearing_date: int = pydantic.Field(
        alias="clearing_date",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    interchange_fees_amount: typing.Optional[int] = pydantic.Field(
        alias="interchange_fees_amount", default=None
    )
    net_total_amount: int = pydantic.Field(
        alias="net_total_amount",
    )
    network: typing.Optional[typing_extensions.Literal["maestro", "visa"]] = (
        pydantic.Field(alias="network", default=None)
    )
    network_settlement_identifier: typing.Optional[str] = pydantic.Field(
        alias="network_settlement_identifier", default=None
    )
    transaction_amount: typing.Optional[int] = pydantic.Field(
        alias="transaction_amount", default=None
    )
    transaction_count: typing.Optional[int] = pydantic.Field(
        alias="transaction_count", default=None
    )
