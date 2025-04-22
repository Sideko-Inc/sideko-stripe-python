import pydantic
import typing
import typing_extensions

from .customer_update_body_cash_balance_settings import (
    CustomerUpdateBodyCashBalanceSettings,
    _SerializerCustomerUpdateBodyCashBalanceSettings,
)


class CustomerUpdateBodyCashBalance(typing_extensions.TypedDict):
    """
    Balance information and default balance settings for this customer.
    """

    settings: typing_extensions.NotRequired[CustomerUpdateBodyCashBalanceSettings]


class _SerializerCustomerUpdateBodyCashBalance(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBodyCashBalance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    settings: typing.Optional[_SerializerCustomerUpdateBodyCashBalanceSettings] = (
        pydantic.Field(alias="settings", default=None)
    )
