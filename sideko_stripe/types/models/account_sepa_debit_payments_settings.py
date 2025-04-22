import pydantic
import typing


class AccountSepaDebitPaymentsSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    creditor_id: typing.Optional[str] = pydantic.Field(
        alias="creditor_id", default=None
    )
    """
    SEPA creditor identifier that identifies the company making the payment.
    """
