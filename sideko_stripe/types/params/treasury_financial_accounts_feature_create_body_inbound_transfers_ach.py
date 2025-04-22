import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
