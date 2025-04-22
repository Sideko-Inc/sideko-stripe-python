import pydantic
import typing
import typing_extensions


class PaymentMethodConfigurationCreateBodySepaDebitDisplayPreference(
    typing_extensions.TypedDict
):
    """
    PaymentMethodConfigurationCreateBodySepaDebitDisplayPreference
    """

    preference: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off", "on"]
    ]


class _SerializerPaymentMethodConfigurationCreateBodySepaDebitDisplayPreference(
    pydantic.BaseModel
):
    """
    Serializer for PaymentMethodConfigurationCreateBodySepaDebitDisplayPreference handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preference: typing.Optional[typing_extensions.Literal["none", "off", "on"]] = (
        pydantic.Field(alias="preference", default=None)
    )
