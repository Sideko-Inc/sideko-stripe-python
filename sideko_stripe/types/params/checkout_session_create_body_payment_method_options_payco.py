import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsPayco(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsPayco
    """

    capture_method: typing_extensions.NotRequired[typing_extensions.Literal["manual"]]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsPayco(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsPayco handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[typing_extensions.Literal["manual"]] = (
        pydantic.Field(alias="capture_method", default=None)
    )
