import pydantic
import typing_extensions


class CheckoutSessionCreateBodyPhoneNumberCollection(typing_extensions.TypedDict):
    """
    Controls phone number collection settings for the session.

    We recommend that you review your privacy policy and check with your legal contacts
    before using this feature. Learn more about [collecting phone numbers with Checkout](https://stripe.com/docs/payments/checkout/phone-numbers).
    """

    enabled: typing_extensions.Required[bool]


class _SerializerCheckoutSessionCreateBodyPhoneNumberCollection(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPhoneNumberCollection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
