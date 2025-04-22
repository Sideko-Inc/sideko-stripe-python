import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0(
    typing_extensions.TypedDict
):
    """
    PaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0
    """

    message: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
