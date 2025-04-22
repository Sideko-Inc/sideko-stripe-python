import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsSofort(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsSofort
    """

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSofort(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsSofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
