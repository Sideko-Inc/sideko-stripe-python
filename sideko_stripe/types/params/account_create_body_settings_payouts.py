import pydantic
import typing
import typing_extensions

from .account_create_body_settings_payouts_schedule import (
    AccountCreateBodySettingsPayoutsSchedule,
    _SerializerAccountCreateBodySettingsPayoutsSchedule,
)


class AccountCreateBodySettingsPayouts(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsPayouts
    """

    debit_negative_balances: typing_extensions.NotRequired[bool]

    schedule: typing_extensions.NotRequired[AccountCreateBodySettingsPayoutsSchedule]

    statement_descriptor: typing_extensions.NotRequired[str]


class _SerializerAccountCreateBodySettingsPayouts(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsPayouts handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    debit_negative_balances: typing.Optional[bool] = pydantic.Field(
        alias="debit_negative_balances", default=None
    )
    schedule: typing.Optional[_SerializerAccountCreateBodySettingsPayoutsSchedule] = (
        pydantic.Field(alias="schedule", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
