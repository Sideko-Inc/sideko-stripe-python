import pydantic
import typing_extensions


class TreasuryFinancialAccountsFeatureCreateBodyCardIssuing(
    typing_extensions.TypedDict
):
    """
    Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
    """

    requested: typing_extensions.Required[bool]


class _SerializerTreasuryFinancialAccountsFeatureCreateBodyCardIssuing(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountsFeatureCreateBodyCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: bool = pydantic.Field(
        alias="requested",
    )
