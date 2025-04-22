import pydantic
import typing
import typing_extensions

from .treasury_financial_accounts_feature_create_body_inbound_transfers_ach import (
    TreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch,
    _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch,
)


class TreasuryFinancialAccountsFeatureCreateBodyInboundTransfers(
    typing_extensions.TypedDict
):
    """
    Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
    """

    ach: typing_extensions.NotRequired[
        TreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch
    ]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfers(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyInboundTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTreasuryFinancialAccountsFeatureCreateBodyInboundTransfersAch
    ] = pydantic.Field(alias="ach", default=None)
