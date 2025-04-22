import pydantic
import typing
import typing_extensions


class ChargeCreateBodyTransferData(typing_extensions.TypedDict):
    """
    An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerChargeCreateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for ChargeCreateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
