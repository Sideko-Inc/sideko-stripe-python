import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_mandate_data_obj0_customer_acceptance_online import (
    SetupIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline,
    _SerializerSetupIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline,
)


class SetupIntentCreateBodyMandateDataObj0CustomerAcceptance(
    typing_extensions.TypedDict
):
    """
    SetupIntentCreateBodyMandateDataObj0CustomerAcceptance
    """

    accepted_at: typing_extensions.NotRequired[int]

    offline: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    online: typing_extensions.NotRequired[
        SetupIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline
    ]

    type_: typing_extensions.Required[typing_extensions.Literal["offline", "online"]]


class _SerializerSetupIntentCreateBodyMandateDataObj0CustomerAcceptance(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentCreateBodyMandateDataObj0CustomerAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accepted_at: typing.Optional[int] = pydantic.Field(
        alias="accepted_at", default=None
    )
    offline: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="offline", default=None
    )
    online: typing.Optional[
        _SerializerSetupIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline
    ] = pydantic.Field(alias="online", default=None)
    type_: typing_extensions.Literal["offline", "online"] = pydantic.Field(
        alias="type",
    )
