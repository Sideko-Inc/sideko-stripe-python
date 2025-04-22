import pydantic
import typing
import typing_extensions


class CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions
    """

    amount: typing_extensions.NotRequired[int]

    amount_type: typing_extensions.NotRequired[
        typing_extensions.Literal["fixed", "maximum"]
    ]

    description: typing_extensions.NotRequired[str]


class _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCardObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    amount_type: typing.Optional[typing_extensions.Literal["fixed", "maximum"]] = (
        pydantic.Field(alias="amount_type", default=None)
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
