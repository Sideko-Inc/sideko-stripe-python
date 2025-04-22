import pydantic
import typing
import typing_extensions


class PaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference(
    typing_extensions.TypedDict
):
    """
    PaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference
    """

    preference: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off", "on"]
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyWechatPayDisplayPreference handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preference: typing.Optional[typing_extensions.Literal["none", "off", "on"]] = (
        pydantic.Field(alias="preference", default=None)
    )
