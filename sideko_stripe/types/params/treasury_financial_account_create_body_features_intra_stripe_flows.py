import pydantic
import typing_extensions


class TreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesIntraStripeFlows handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
