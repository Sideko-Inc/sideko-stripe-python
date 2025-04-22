import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodySavedPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Controls saved payment method settings for the session. Only available in `payment` and `subscription` mode.
    """

    allow_redisplay_filters: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["always", "limited", "unspecified"]]
    ]

    payment_method_save: typing_extensions.NotRequired[
        typing_extensions.Literal["disabled", "enabled"]
    ]


class _SerializerCheckoutSessionCreateBodySavedPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodySavedPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_redisplay_filters: typing.Optional[
        typing.List[typing_extensions.Literal["always", "limited", "unspecified"]]
    ] = pydantic.Field(alias="allow_redisplay_filters", default=None)
    payment_method_save: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_save", default=None)
