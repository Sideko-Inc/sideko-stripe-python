import pydantic
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
