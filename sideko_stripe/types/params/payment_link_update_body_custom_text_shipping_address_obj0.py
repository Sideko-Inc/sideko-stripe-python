import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomTextShippingAddressObj0(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomTextShippingAddressObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyCustomTextShippingAddressObj0(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomTextShippingAddressObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
