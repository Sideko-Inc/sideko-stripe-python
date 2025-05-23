import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0
    """

    preferred_language: typing_extensions.NotRequired[
        typing_extensions.Literal["de", "en", "fr", "nl"]
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsBancontactObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred_language: typing.Optional[
        typing_extensions.Literal["de", "en", "fr", "nl"]
    ] = pydantic.Field(alias="preferred_language", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
