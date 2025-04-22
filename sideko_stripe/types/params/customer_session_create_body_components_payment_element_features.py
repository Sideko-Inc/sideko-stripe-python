import pydantic
import typing
import typing_extensions


class CustomerSessionCreateBodyComponentsPaymentElementFeatures(
    typing_extensions.TypedDict
):
    """
    CustomerSessionCreateBodyComponentsPaymentElementFeatures
    """

    payment_method_allow_redisplay_filters: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["always", "limited", "unspecified"]]
    ]

    payment_method_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["disabled", "enabled"]
    ]

    payment_method_redisplay_limit: typing_extensions.NotRequired[int]

    payment_method_remove: typing_extensions.NotRequired[
        typing_extensions.Literal["disabled", "enabled"]
    ]

    payment_method_save: typing_extensions.NotRequired[
        typing_extensions.Literal["disabled", "enabled"]
    ]

    payment_method_save_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]


class _SerializerCustomerSessionCreateBodyComponentsPaymentElementFeatures(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSessionCreateBodyComponentsPaymentElementFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payment_method_allow_redisplay_filters: typing.Optional[
        typing.List[typing_extensions.Literal["always", "limited", "unspecified"]]
    ] = pydantic.Field(alias="payment_method_allow_redisplay_filters", default=None)
    payment_method_redisplay: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_redisplay", default=None)
    payment_method_redisplay_limit: typing.Optional[int] = pydantic.Field(
        alias="payment_method_redisplay_limit", default=None
    )
    payment_method_remove: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_remove", default=None)
    payment_method_save: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_save", default=None)
    payment_method_save_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="payment_method_save_usage", default=None)
