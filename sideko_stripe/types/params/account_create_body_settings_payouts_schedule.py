import pydantic
import typing
import typing_extensions


class AccountCreateBodySettingsPayoutsSchedule(typing_extensions.TypedDict):
    """
    AccountCreateBodySettingsPayoutsSchedule
    """

    delay_days: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["minimum"], int]
    ]

    interval: typing_extensions.NotRequired[
        typing_extensions.Literal["daily", "manual", "monthly", "weekly"]
    ]

    monthly_anchor: typing_extensions.NotRequired[int]

    weekly_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
        ]
    ]


class _SerializerAccountCreateBodySettingsPayoutsSchedule(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodySettingsPayoutsSchedule handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    delay_days: typing.Optional[
        typing.Union[typing_extensions.Literal["minimum"], int]
    ] = pydantic.Field(alias="delay_days", default=None)
    interval: typing.Optional[
        typing_extensions.Literal["daily", "manual", "monthly", "weekly"]
    ] = pydantic.Field(alias="interval", default=None)
    monthly_anchor: typing.Optional[int] = pydantic.Field(
        alias="monthly_anchor", default=None
    )
    weekly_anchor: typing.Optional[
        typing_extensions.Literal[
            "friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"
        ]
    ] = pydantic.Field(alias="weekly_anchor", default=None)
