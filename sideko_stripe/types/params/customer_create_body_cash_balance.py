import pydantic
import typing
import typing_extensions

from .customer_create_body_cash_balance_settings import (
    CustomerCreateBodyCashBalanceSettings,
    _SerializerCustomerCreateBodyCashBalanceSettings,
)


class CustomerCreateBodyCashBalance(typing_extensions.TypedDict):
    """
    Balance information and default balance settings for this customer.
    """

    settings: typing_extensions.NotRequired[CustomerCreateBodyCashBalanceSettings]


class _SerializerCustomerCreateBodyCashBalance(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBodyCashBalance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    settings: typing.Optional[_SerializerCustomerCreateBodyCashBalanceSettings] = (
        pydantic.Field(alias="settings", default=None)
    )
