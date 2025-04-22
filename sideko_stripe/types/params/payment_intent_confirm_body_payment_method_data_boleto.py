import pydantic
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
