import pydantic


class PaymentMethodDetailsBoleto(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
    """
    The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses consumers)
    """
