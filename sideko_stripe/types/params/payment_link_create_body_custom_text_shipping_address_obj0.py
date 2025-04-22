import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomTextShippingAddressObj0(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomTextShippingAddressObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyCustomTextShippingAddressObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomTextShippingAddressObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
