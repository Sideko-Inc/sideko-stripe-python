import pydantic
import typing_extensions

from .payment_link_create_body_restrictions_completed_sessions import (
    PaymentLinkCreateBodyRestrictionsCompletedSessions,
    _SerializerPaymentLinkCreateBodyRestrictionsCompletedSessions,
)


class PaymentLinkCreateBodyRestrictions(typing_extensions.TypedDict):
    """
    Settings that restrict the usage of a payment link.
    """

    completed_sessions: typing_extensions.Required[
        PaymentLinkCreateBodyRestrictionsCompletedSessions
    ]


class _SerializerPaymentLinkCreateBodyRestrictions(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyRestrictions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    completed_sessions: _SerializerPaymentLinkCreateBodyRestrictionsCompletedSessions = pydantic.Field(
        alias="completed_sessions",
    )
