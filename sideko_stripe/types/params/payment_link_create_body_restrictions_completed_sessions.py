import pydantic
import typing_extensions


class PaymentLinkCreateBodyRestrictionsCompletedSessions(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyRestrictionsCompletedSessions
    """

    limit: typing_extensions.Required[int]


class _SerializerPaymentLinkCreateBodyRestrictionsCompletedSessions(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyRestrictionsCompletedSessions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    limit: int = pydantic.Field(
        alias="limit",
    )
