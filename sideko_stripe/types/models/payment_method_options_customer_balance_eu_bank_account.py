import pydantic
import typing_extensions


class PaymentMethodOptionsCustomerBalanceEuBankAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing_extensions.Literal["BE", "DE", "ES", "FR", "IE", "NL"] = (
        pydantic.Field(
            alias="country",
        )
    )
    """
    The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
    """
