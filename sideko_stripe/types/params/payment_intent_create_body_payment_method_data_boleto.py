import pydantic
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
