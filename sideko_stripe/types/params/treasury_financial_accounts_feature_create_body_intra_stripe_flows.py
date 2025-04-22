import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows(
    typing_extensions.TypedDict
):
    """
    Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyIntraStripeFlows handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
