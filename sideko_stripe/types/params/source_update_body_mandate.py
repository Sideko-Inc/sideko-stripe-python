import pydantic
import typing
import typing_extensions

from .source_update_body_mandate_acceptance import (
    SourceUpdateBodyMandateAcceptance,
    _SerializerSourceUpdateBodyMandateAcceptance,
)


class SourceUpdateBodyMandate(typing_extensions.TypedDict):
    """
    Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    """

    acceptance: typing_extensions.NotRequired[SourceUpdateBodyMandateAcceptance]

    amount: typing_extensions.NotRequired[typing.Union[int, str]]

    currency: typing_extensions.NotRequired[str]

    interval: typing_extensions.NotRequired[
        typing_extensions.Literal["one_time", "scheduled", "variable"]
    ]

    notification_method: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "deprecated_none", "email", "manual", "none", "stripe_email"
        ]
    ]


class _SerializerSourceUpdateBodyMandate(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBodyMandate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acceptance: typing.Optional[_SerializerSourceUpdateBodyMandateAcceptance] = (
        pydantic.Field(alias="acceptance", default=None)
    )
    amount: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="amount", default=None
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    interval: typing.Optional[
        typing_extensions.Literal["one_time", "scheduled", "variable"]
    ] = pydantic.Field(alias="interval", default=None)
    notification_method: typing.Optional[
        typing_extensions.Literal[
            "deprecated_none", "email", "manual", "none", "stripe_email"
        ]
    ] = pydantic.Field(alias="notification_method", default=None)
