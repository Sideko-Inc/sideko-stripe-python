import pydantic
import typing_extensions


class TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
