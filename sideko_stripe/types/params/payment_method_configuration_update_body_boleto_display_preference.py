import pydantic
import typing
import typing_extensions


class PaymentMethodConfigurationUpdateBodyBoletoDisplayPreference(
    typing_extensions.TypedDict
):
    """
    PaymentMethodConfigurationUpdateBodyBoletoDisplayPreference
    """

    preference: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off", "on"]
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyBoletoDisplayPreference(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyBoletoDisplayPreference handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preference: typing.Optional[typing_extensions.Literal["none", "off", "on"]] = (
        pydantic.Field(alias="preference", default=None)
    )
