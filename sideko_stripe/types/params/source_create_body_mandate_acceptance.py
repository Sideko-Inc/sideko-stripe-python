import pydantic
import typing
import typing_extensions

from .source_create_body_mandate_acceptance_offline import (
    SourceCreateBodyMandateAcceptanceOffline,
    _SerializerSourceCreateBodyMandateAcceptanceOffline,
)
from .source_create_body_mandate_acceptance_online import (
    SourceCreateBodyMandateAcceptanceOnline,
    _SerializerSourceCreateBodyMandateAcceptanceOnline,
)


class SourceCreateBodyMandateAcceptance(typing_extensions.TypedDict):
    """
    SourceCreateBodyMandateAcceptance
    """

    date: typing_extensions.NotRequired[int]

    ip: typing_extensions.NotRequired[str]

    offline: typing_extensions.NotRequired[SourceCreateBodyMandateAcceptanceOffline]

    online: typing_extensions.NotRequired[SourceCreateBodyMandateAcceptanceOnline]

    status: typing_extensions.Required[
        typing_extensions.Literal["accepted", "pending", "refused", "revoked"]
    ]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["offline", "online"]]

    user_agent: typing_extensions.NotRequired[str]


class _SerializerSourceCreateBodyMandateAcceptance(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyMandateAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    offline: typing.Optional[_SerializerSourceCreateBodyMandateAcceptanceOffline] = (
        pydantic.Field(alias="offline", default=None)
    )
    online: typing.Optional[_SerializerSourceCreateBodyMandateAcceptanceOnline] = (
        pydantic.Field(alias="online", default=None)
    )
    status: typing_extensions.Literal["accepted", "pending", "refused", "revoked"] = (
        pydantic.Field(
            alias="status",
        )
    )
    type_: typing.Optional[typing_extensions.Literal["offline", "online"]] = (
        pydantic.Field(alias="type", default=None)
    )
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
