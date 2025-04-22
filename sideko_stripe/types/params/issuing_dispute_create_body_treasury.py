import pydantic
import typing_extensions


class IssuingDisputeCreateBodyTreasury(typing_extensions.TypedDict):
    """
    Params for disputes related to Treasury FinancialAccounts
    """

    received_debit: typing_extensions.Required[str]


class _SerializerIssuingDisputeCreateBodyTreasury(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeCreateBodyTreasury handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    received_debit: str = pydantic.Field(
        alias="received_debit",
    )
