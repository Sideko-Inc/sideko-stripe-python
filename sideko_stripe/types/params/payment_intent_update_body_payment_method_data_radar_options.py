import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodDataRadarOptions(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataRadarOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
