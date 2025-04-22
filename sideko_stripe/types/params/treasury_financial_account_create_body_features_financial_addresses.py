import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features_financial_addresses_aba import (
    TreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba,
    _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba,
)


class TreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses(
    typing_extensions.TypedDict
):
    """
    TreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses
    """

    aba: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba
    ]


class _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountCreateBodyFeaturesFinancialAddresses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aba: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyFeaturesFinancialAddressesAba
    ] = pydantic.Field(alias="aba", default=None)
