import pydantic
import typing_extensions


class TreasuryReceivedCreditListLinkedFlows(typing_extensions.TypedDict):
    """
    Only return ReceivedCredits described by the flow.
    """

    source_flow_type: typing_extensions.Required[
        typing_extensions.Literal[
            "credit_reversal",
            "other",
            "outbound_payment",
            "outbound_transfer",
            "payout",
        ]
    ]


class _SerializerTreasuryReceivedCreditListLinkedFlows(pydantic.BaseModel):
    """
    Serializer for TreasuryReceivedCreditListLinkedFlows handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    source_flow_type: typing_extensions.Literal[
        "credit_reversal", "other", "outbound_payment", "outbound_transfer", "payout"
    ] = pydantic.Field(
        alias="source_flow_type",
    )
