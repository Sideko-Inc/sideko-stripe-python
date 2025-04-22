import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomTextSubmitObj0(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomTextSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyCustomTextSubmitObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomTextSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
