import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0
    """

    confirmation_number: typing_extensions.NotRequired[typing.Union[str, str]]

    expires_after_days: typing_extensions.NotRequired[typing.Union[int, str]]

    expires_at: typing_extensions.NotRequired[typing.Union[int, str]]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsKonbiniObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    confirmation_number: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="confirmation_number", default=None
    )
    expires_after_days: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="expires_after_days", default=None
    )
    expires_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="expires_at", default=None
    )
    product_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="product_description", default=None
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
