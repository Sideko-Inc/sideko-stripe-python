import pydantic
import typing
import typing_extensions

from .customer_cash_balance_modify_body_settings import (
    CustomerCashBalanceModifyBodySettings,
    _SerializerCustomerCashBalanceModifyBodySettings,
)


class CustomerCashBalanceModifyBody(typing_extensions.TypedDict, total=False):
    """
    CustomerCashBalanceModifyBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    settings: typing_extensions.NotRequired[CustomerCashBalanceModifyBodySettings]
    """
    A hash of settings for this cash balance.
    """


class _SerializerCustomerCashBalanceModifyBody(pydantic.BaseModel):
    """
    Serializer for CustomerCashBalanceModifyBody handling case conversions
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
    settings: typing.Optional[_SerializerCustomerCashBalanceModifyBodySettings] = (
        pydantic.Field(alias="settings", default=None)
    )
