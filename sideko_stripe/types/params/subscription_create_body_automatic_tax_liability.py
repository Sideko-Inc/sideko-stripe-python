import pydantic
import typing
import typing_extensions


class SubscriptionCreateBodyAutomaticTaxLiability(typing_extensions.TypedDict):
    """
    SubscriptionCreateBodyAutomaticTaxLiability
    """

    account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "self"]]


class _SerializerSubscriptionCreateBodyAutomaticTaxLiability(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyAutomaticTaxLiability handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
