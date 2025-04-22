import pydantic
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataSofort(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataSofort
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataSofort(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataSofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"] = (
        pydantic.Field(
            alias="country",
        )
    )
