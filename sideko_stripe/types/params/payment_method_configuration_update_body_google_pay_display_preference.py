import pydantic
import typing
import typing_extensions


class PaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference(
    typing_extensions.TypedDict
):
    """
    PaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference
    """

    preference: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off", "on"]
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preference: typing.Optional[typing_extensions.Literal["none", "off", "on"]] = (
        pydantic.Field(alias="preference", default=None)
    )
