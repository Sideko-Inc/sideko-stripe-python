import pydantic
import typing_extensions


class CheckoutSessionCreateBodyCustomTextShippingAddressObj0(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyCustomTextShippingAddressObj0
    """

    message: typing_extensions.Required[str]


class _SerializerCheckoutSessionCreateBodyCustomTextShippingAddressObj0(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyCustomTextShippingAddressObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
