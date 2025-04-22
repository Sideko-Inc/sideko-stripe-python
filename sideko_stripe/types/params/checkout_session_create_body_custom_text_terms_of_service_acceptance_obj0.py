import pydantic
import typing_extensions


class CheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0
    """

    message: typing_extensions.Required[str]


class _SerializerCheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
