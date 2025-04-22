import pydantic
import typing_extensions


class CheckoutSessionCreateBodyCustomTextSubmitObj0(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyCustomTextSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerCheckoutSessionCreateBodyCustomTextSubmitObj0(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomTextSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
