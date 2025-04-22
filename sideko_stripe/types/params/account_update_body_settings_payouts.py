import pydantic
import typing
import typing_extensions

from .account_update_body_settings_payouts_schedule import (
    AccountUpdateBodySettingsPayoutsSchedule,
    _SerializerAccountUpdateBodySettingsPayoutsSchedule,
)


class AccountUpdateBodySettingsPayouts(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsPayouts
    """

    debit_negative_balances: typing_extensions.NotRequired[bool]

    schedule: typing_extensions.NotRequired[AccountUpdateBodySettingsPayoutsSchedule]

    statement_descriptor: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateBodySettingsPayouts(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsPayouts handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    debit_negative_balances: typing.Optional[bool] = pydantic.Field(
        alias="debit_negative_balances", default=None
    )
    schedule: typing.Optional[_SerializerAccountUpdateBodySettingsPayoutsSchedule] = (
        pydantic.Field(alias="schedule", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
