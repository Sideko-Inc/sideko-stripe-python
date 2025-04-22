import pydantic
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataKlarnaDob(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataKlarnaDob
    """

    day: typing_extensions.Required[int]

    month: typing_extensions.Required[int]

    year: typing_extensions.Required[int]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarnaDob(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataKlarnaDob handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: int = pydantic.Field(
        alias="day",
    )
    month: int = pydantic.Field(
        alias="month",
    )
    year: int = pydantic.Field(
        alias="year",
    )
