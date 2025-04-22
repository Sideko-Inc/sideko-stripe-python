import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomTextAfterSubmitObj0(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomTextAfterSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyCustomTextAfterSubmitObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomTextAfterSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
