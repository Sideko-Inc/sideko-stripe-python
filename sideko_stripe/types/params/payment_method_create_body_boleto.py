import pydantic
import typing_extensions


class PaymentMethodCreateBodyBoleto(typing_extensions.TypedDict):
    """
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    """

    tax_id: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodyBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
