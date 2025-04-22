import pydantic
import typing

from .payment_method_us_bank_account_blocked import PaymentMethodUsBankAccountBlocked


class PaymentMethodUsBankAccountStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    blocked: typing.Optional[PaymentMethodUsBankAccountBlocked] = pydantic.Field(
        alias="blocked", default=None
    )
