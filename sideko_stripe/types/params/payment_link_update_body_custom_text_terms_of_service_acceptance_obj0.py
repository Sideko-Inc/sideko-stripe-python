import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
