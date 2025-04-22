import pydantic
import typing_extensions


class CheckoutSessionCreateBodyCustomTextAfterSubmitObj0(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyCustomTextAfterSubmitObj0
    """

    message: typing_extensions.Required[str]


class _SerializerCheckoutSessionCreateBodyCustomTextAfterSubmitObj0(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomTextAfterSubmitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
