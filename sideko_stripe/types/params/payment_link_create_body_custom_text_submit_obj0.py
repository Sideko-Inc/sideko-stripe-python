import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomTextSubmitObj0(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomTextSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyCustomTextSubmitObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomTextSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
