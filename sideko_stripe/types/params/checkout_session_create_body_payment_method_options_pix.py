import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsPix(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsPix
    """

    expires_after_seconds: typing_extensions.NotRequired[int]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPix(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsPix handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expires_after_seconds: typing.Optional[int] = pydantic.Field(
        alias="expires_after_seconds", default=None
    )
