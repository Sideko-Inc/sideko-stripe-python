import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_feature_create_body_financial_addresses_aba import (
    TreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba,
)


class TreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses(
    typing_extensions.TypedDict
):
    """
    Contains Features that add FinancialAddresses to the FinancialAccount.
    """

    aba: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba
    ]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyFinancialAddresses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aba: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyFinancialAddressesAba
    ] = pydantic.Field(alias="aba", default=None)
