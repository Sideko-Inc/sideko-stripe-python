import pydantic
import typing
import typing_extensions


class TreasuryFinancialAccountUpdateBodyForwardingSettings(typing_extensions.TypedDict):
    """
    A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0
    """

    financial_account: typing_extensions.NotRequired[str]

    payment_method: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[
        typing_extensions.Literal["financial_account", "payment_method"]
    ]


class _SerializerTreasuryFinancialAccountUpdateBodyForwardingSettings(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryFinancialAccountUpdateBodyForwardingSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    type_: typing_extensions.Literal["financial_account", "payment_method"] = (
        pydantic.Field(
            alias="type",
        )
    )
