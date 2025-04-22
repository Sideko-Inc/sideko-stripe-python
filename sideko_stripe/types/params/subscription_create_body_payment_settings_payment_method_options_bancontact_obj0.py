import pydantic
import typing
import typing_extensions


class SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0
    """

    preferred_language: typing_extensions.NotRequired[
        typing_extensions.Literal["de", "en", "fr", "nl"]
    ]


class _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsBancontactObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred_language: typing.Optional[
        typing_extensions.Literal["de", "en", "fr", "nl"]
    ] = pydantic.Field(alias="preferred_language", default=None)
