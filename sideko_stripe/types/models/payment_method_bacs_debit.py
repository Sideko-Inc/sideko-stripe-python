import pydantic
import typing


class PaymentMethodBacsDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    Last four digits of the bank account number.
    """
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
    """
    Sort code of the bank account. (e.g., `10-20-30`)
    """
