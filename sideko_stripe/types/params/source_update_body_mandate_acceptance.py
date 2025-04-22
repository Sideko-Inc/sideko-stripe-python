import pydantic
import typing
import typing_extensions

from .source_update_body_mandate_acceptance_offline import (
    SourceUpdateBodyMandateAcceptanceOffline,
    _SerializerSourceUpdateBodyMandateAcceptanceOffline,
)
from .source_update_body_mandate_acceptance_online import (
    SourceUpdateBodyMandateAcceptanceOnline,
    _SerializerSourceUpdateBodyMandateAcceptanceOnline,
)


class SourceUpdateBodyMandateAcceptance(typing_extensions.TypedDict):
    """
    SourceUpdateBodyMandateAcceptance
    """

    date: typing_extensions.NotRequired[int]

    ip: typing_extensions.NotRequired[str]

    offline: typing_extensions.NotRequired[SourceUpdateBodyMandateAcceptanceOffline]

    online: typing_extensions.NotRequired[SourceUpdateBodyMandateAcceptanceOnline]

    status: typing_extensions.Required[
        typing_extensions.Literal["accepted", "pending", "refused", "revoked"]
    ]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["offline", "online"]]

    user_agent: typing_extensions.NotRequired[str]


class _SerializerSourceUpdateBodyMandateAcceptance(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBodyMandateAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    offline: typing.Optional[_SerializerSourceUpdateBodyMandateAcceptanceOffline] = (
        pydantic.Field(alias="offline", default=None)
    )
    online: typing.Optional[_SerializerSourceUpdateBodyMandateAcceptanceOnline] = (
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
