import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features_financial_addresses_aba import (
    TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba,
    _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba,
)


class TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses
    """

    aba: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyFeaturesFinancialAddresses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aba: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyFeaturesFinancialAddressesAba
    ] = pydantic.Field(alias="aba", default=None)
