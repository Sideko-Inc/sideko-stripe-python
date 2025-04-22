import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyDepositInsurance(
    typing_extensions.TypedDict
):
    """
    Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyDepositInsurance(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyDepositInsurance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
