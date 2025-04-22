import pydantic
import typing_extensions


class TreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
