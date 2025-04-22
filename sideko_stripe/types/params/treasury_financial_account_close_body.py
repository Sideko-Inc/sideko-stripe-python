import pydantic
import typing
import typing_extensions

from .treasury_financial_account_close_body_forwarding_settings import (
    TreasuryFinancialAccountCloseBodyForwardingSettings,
    _SerializerTreasuryFinancialAccountCloseBodyForwardingSettings,
)


class TreasuryFinancialAccountCloseBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryFinancialAccountCloseBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    forwarding_settings: typing_extensions.NotRequired[
        TreasuryFinancialAccountCloseBodyForwardingSettings
    ]
    """
    A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0
    """


class _SerializerTreasuryFinancialAccountCloseBody(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountCloseBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    forwarding_settings: typing.Optional[
        _SerializerTreasuryFinancialAccountCloseBodyForwardingSettings
    ] = pydantic.Field(alias="forwarding_settings", default=None)
