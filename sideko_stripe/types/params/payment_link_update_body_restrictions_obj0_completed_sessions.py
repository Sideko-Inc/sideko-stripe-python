import pydantic
import typing_extensions


class PaymentLinkUpdateBodyRestrictionsObj0CompletedSessions(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodyRestrictionsObj0CompletedSessions
    """

    limit: typing_extensions.Required[int]


class _SerializerPaymentLinkUpdateBodyRestrictionsObj0CompletedSessions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodyRestrictionsObj0CompletedSessions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    limit: int = pydantic.Field(
        alias="limit",
    )
