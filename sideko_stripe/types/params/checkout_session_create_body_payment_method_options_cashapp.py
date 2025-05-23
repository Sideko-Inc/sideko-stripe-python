import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsCashapp(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsCashapp
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCashapp(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsCashapp handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
