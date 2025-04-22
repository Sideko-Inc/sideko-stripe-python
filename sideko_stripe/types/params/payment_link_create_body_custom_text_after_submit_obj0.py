import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomTextAfterSubmitObj0(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomTextAfterSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyCustomTextAfterSubmitObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomTextAfterSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
