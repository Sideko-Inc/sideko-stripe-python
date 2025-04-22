import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsSofortObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsSofortObj0
    """

    preferred_language: typing_extensions.NotRequired[
        typing_extensions.Literal["de", "en", "es", "fr", "it", "nl", "pl"]
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSofortObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsSofortObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred_language: typing.Optional[
        typing_extensions.Literal["de", "en", "es", "fr", "it", "nl", "pl"]
    ] = pydantic.Field(alias="preferred_language", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
