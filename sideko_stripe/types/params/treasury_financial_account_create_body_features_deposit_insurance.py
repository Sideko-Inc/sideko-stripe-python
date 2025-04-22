import pydantic
import typing_extensions


class TreasuryFinancialAccountCreateBodyFeaturesDepositInsurance(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesDepositInsurance
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesDepositInsurance(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesDepositInsurance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
