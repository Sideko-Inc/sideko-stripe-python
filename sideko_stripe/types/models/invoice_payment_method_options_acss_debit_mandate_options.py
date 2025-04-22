import pydantic
import typing
import typing_extensions


class InvoicePaymentMethodOptionsAcssDebitMandateOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    transaction_type: typing.Optional[
        typing_extensions.Literal["business", "personal"]
    ] = pydantic.Field(alias="transaction_type", default=None)
    """
    Transaction type of the mandate.
    """
