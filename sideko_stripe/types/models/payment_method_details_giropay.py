import pydantic
import typing


class PaymentMethodDetailsGiropay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_code: typing.Optional[str] = pydantic.Field(alias="bank_code", default=None)
    """
    Bank code of bank associated with the bank account.
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Name of the bank associated with the bank account.
    """
    bic: typing.Optional[str] = pydantic.Field(alias="bic", default=None)
    """
    Bank Identifier Code of the bank associated with the bank account.
    """
    verified_name: typing.Optional[str] = pydantic.Field(
        alias="verified_name", default=None
    )
    """
    Owner's verified full name. Values are verified or provided by Giropay directly
    (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    Giropay rarely provides this information so the attribute is usually empty.
    """
