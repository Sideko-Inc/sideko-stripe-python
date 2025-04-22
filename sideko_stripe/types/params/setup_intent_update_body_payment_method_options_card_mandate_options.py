import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions
    """

    amount: typing_extensions.Required[int]

    amount_type: typing_extensions.Required[
        typing_extensions.Literal["fixed", "maximum"]
    ]

    currency: typing_extensions.Required[str]

    description: typing_extensions.NotRequired[str]

    end_date: typing_extensions.NotRequired[int]

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "sporadic", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]

    reference: typing_extensions.Required[str]

    start_date: typing_extensions.Required[int]

    supported_types: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["india"]]
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsCardMandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    amount_type: typing_extensions.Literal["fixed", "maximum"] = pydantic.Field(
        alias="amount_type",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    end_date: typing.Optional[int] = pydantic.Field(alias="end_date", default=None)
    interval: typing_extensions.Literal["day", "month", "sporadic", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    reference: str = pydantic.Field(
        alias="reference",
    )
    start_date: int = pydantic.Field(
        alias="start_date",
    )
    supported_types: typing.Optional[
        typing.List[typing_extensions.Literal["india"]]
    ] = pydantic.Field(alias="supported_types", default=None)
