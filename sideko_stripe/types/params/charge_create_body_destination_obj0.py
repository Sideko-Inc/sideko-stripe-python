import pydantic
import typing
import typing_extensions


class ChargeCreateBodyDestinationObj0(typing_extensions.TypedDict):
    """
    ChargeCreateBodyDestinationObj0
    """

    account: typing_extensions.Required[str]

    amount: typing_extensions.NotRequired[int]


class _SerializerChargeCreateBodyDestinationObj0(pydantic.BaseModel):
    """
    Serializer for ChargeCreateBodyDestinationObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: str = pydantic.Field(
        alias="account",
    )
    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
