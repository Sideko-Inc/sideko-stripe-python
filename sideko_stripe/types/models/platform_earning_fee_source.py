import pydantic
import typing
import typing_extensions


class PlatformEarningFeeSource(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: typing.Optional[str] = pydantic.Field(alias="charge", default=None)
    """
    Charge ID that created this application fee.
    """
    payout: typing.Optional[str] = pydantic.Field(alias="payout", default=None)
    """
    Payout ID that created this application fee.
    """
    type_: typing_extensions.Literal["charge", "payout"] = pydantic.Field(
        alias="type",
    )
    """
    Type of object that created the application fee.
    """
