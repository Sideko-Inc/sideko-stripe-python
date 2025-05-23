import pydantic
import typing
import typing_extensions


class SubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability
    """

    account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "self"]]


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemAutomaticTaxLiability handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
