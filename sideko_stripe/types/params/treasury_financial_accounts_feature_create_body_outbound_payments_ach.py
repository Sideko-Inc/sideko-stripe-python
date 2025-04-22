import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyOutboundPaymentsAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
