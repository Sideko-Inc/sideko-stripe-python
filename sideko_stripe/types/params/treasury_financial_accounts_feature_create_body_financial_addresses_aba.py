import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
