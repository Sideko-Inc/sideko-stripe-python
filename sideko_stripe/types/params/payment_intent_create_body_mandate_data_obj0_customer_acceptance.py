import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_mandate_data_obj0_customer_acceptance_online import (
    PaymentIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline,
    _SerializerPaymentIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline,
)


class PaymentIntentCreateBodyMandateDataObj0CustomerAcceptance(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyMandateDataObj0CustomerAcceptance
    """

    accepted_at: typing_extensions.NotRequired[int]

    offline: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    online: typing_extensions.NotRequired[
        PaymentIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline
    ]

    type_: typing_extensions.Required[typing_extensions.Literal["offline", "online"]]


class _SerializerPaymentIntentCreateBodyMandateDataObj0CustomerAcceptance(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyMandateDataObj0CustomerAcceptance handling case conversions
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
        _SerializerPaymentIntentCreateBodyMandateDataObj0CustomerAcceptanceOnline
    ] = pydantic.Field(alias="online", default=None)
    type_: typing_extensions.Literal["offline", "online"] = pydantic.Field(
        alias="type",
    )
