import pydantic
import typing_extensions


class TreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesIntraStripeFlows handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
