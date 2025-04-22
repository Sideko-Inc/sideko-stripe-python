import pydantic


class PaymentMethodBoleto(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
    """
    Uniquely identifies the customer tax id (CNPJ or CPF)
    """
