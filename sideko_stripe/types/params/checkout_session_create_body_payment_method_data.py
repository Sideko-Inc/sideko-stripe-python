import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodData(typing_extensions.TypedDict):
    """
    This parameter allows you to set some attributes on the payment method created during a Checkout session.
    """

    allow_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodData(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
