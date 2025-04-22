import pydantic
import typing
import typing_extensions

from .online_acceptance import OnlineAcceptance


class CustomerAcceptance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accepted_at: typing.Optional[int] = pydantic.Field(
        alias="accepted_at", default=None
    )
    """
    The time that the customer accepts the mandate.
    """
    offline: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="offline", default=None
    )
    online: typing.Optional[OnlineAcceptance] = pydantic.Field(
        alias="online", default=None
    )
    type_: typing_extensions.Literal["offline", "online"] = pydantic.Field(
        alias="type",
    )
    """
    The mandate includes the type of customer acceptance information, such as: `online` or `offline`.
    """
