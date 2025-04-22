import pydantic
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataSofort(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataSofort
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataSofort(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataSofort handling case conversions
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
