import pydantic
import typing_extensions


class PaymentLinkUpdateBodyPhoneNumberCollection(typing_extensions.TypedDict):
    """
    Controls phone number collection settings during checkout.

    We recommend that you review your privacy policy and check with your legal contacts.
    """

    enabled: typing_extensions.Required[bool]


class _SerializerPaymentLinkUpdateBodyPhoneNumberCollection(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyPhoneNumberCollection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
