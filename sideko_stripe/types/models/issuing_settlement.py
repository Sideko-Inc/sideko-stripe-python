import pydantic
import typing_extensions

from .issuing_settlement_metadata import IssuingSettlementMetadata


class IssuingSettlement(pydantic.BaseModel):
    """
    When a non-stripe BIN is used, any use of an [issued card](https://stripe.com/docs/issuing) must be settled directly with the card network. The net amount owed is represented by an Issuing `Settlement` object.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bin: str = pydantic.Field(
        alias="bin",
    )
    """
    The Bank Identification Number reflecting this settlement record.
    """
    clearing_date: int = pydantic.Field(
        alias="clearing_date",
    )
    """
    The date that the transactions are cleared and posted to user's accounts.
    """
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
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    interchange_fees_amount: int = pydantic.Field(
        alias="interchange_fees_amount",
    )
    """
    The total interchange received as reimbursement for the transactions.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: IssuingSettlementMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    net_total_amount: int = pydantic.Field(
        alias="net_total_amount",
    )
    """
    The total net amount required to settle with the network.
    """
    network: typing_extensions.Literal["maestro", "visa"] = pydantic.Field(
        alias="network",
    )
    """
    The card network for this settlement report. One of ["visa", "maestro"]
    """
    network_fees_amount: int = pydantic.Field(
        alias="network_fees_amount",
    )
    """
    The total amount of fees owed to the network.
    """
    network_settlement_identifier: str = pydantic.Field(
        alias="network_settlement_identifier",
    )
    """
    The Settlement Identification Number assigned by the network.
    """
    object: typing_extensions.Literal["issuing.settlement"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    settlement_service: str = pydantic.Field(
        alias="settlement_service",
    )
    """
    One of `international` or `uk_national_net`.
    """
    status: typing_extensions.Literal["complete", "pending"] = pydantic.Field(
        alias="status",
    )
    """
    The current processing status of this settlement.
    """
    transaction_amount: int = pydantic.Field(
        alias="transaction_amount",
    )
    """
    The total transaction amount reflected in this settlement.
    """
    transaction_count: int = pydantic.Field(
        alias="transaction_count",
    )
    """
    The total number of transactions reflected in this settlement.
    """
