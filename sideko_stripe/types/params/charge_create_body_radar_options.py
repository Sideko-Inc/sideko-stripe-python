import pydantic
import typing
import typing_extensions


class ChargeCreateBodyRadarOptions(typing_extensions.TypedDict):
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """

    session: typing_extensions.NotRequired[str]


class _SerializerChargeCreateBodyRadarOptions(pydantic.BaseModel):
    """
    Serializer for ChargeCreateBodyRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
