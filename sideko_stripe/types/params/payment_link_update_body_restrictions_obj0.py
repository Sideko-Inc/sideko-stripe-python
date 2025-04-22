import pydantic
import typing_extensions

from .payment_link_update_body_restrictions_obj0_completed_sessions import (
    PaymentLinkUpdateBodyRestrictionsObj0CompletedSessions,
    _SerializerPaymentLinkUpdateBodyRestrictionsObj0CompletedSessions,
)


class PaymentLinkUpdateBodyRestrictionsObj0(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyRestrictionsObj0
    """

    completed_sessions: typing_extensions.Required[
        PaymentLinkUpdateBodyRestrictionsObj0CompletedSessions
    ]


class _SerializerPaymentLinkUpdateBodyRestrictionsObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyRestrictionsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    completed_sessions: _SerializerPaymentLinkUpdateBodyRestrictionsObj0CompletedSessions = pydantic.Field(
        alias="completed_sessions",
    )
