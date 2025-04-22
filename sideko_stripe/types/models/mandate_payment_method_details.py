import pydantic
import typing

from .mandate_acss_debit import MandateAcssDebit
from .mandate_au_becs_debit import MandateAuBecsDebit
from .mandate_bacs_debit import MandateBacsDebit
from .mandate_paypal import MandatePaypal
from .mandate_sepa_debit import MandateSepaDebit
from .mandate_us_bank_account import MandateUsBankAccount


class MandatePaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[MandateAcssDebit] = pydantic.Field(
        alias="acss_debit", default=None
    )
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[MandateAuBecsDebit] = pydantic.Field(
        alias="au_becs_debit", default=None
    )
    bacs_debit: typing.Optional[MandateBacsDebit] = pydantic.Field(
        alias="bacs_debit", default=None
    )
    card: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="card", default=None
    )
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    kr_card: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    naver_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="naver_pay", default=None
    )
    nz_bank_account: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="nz_bank_account", default=None
    )
    paypal: typing.Optional[MandatePaypal] = pydantic.Field(
        alias="paypal", default=None
    )
    revolut_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="revolut_pay", default=None
    )
    sepa_debit: typing.Optional[MandateSepaDebit] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    This mandate corresponds with a specific payment method type. The `payment_method_details` includes an additional hash with the same name and contains mandate information that's specific to that payment method.
    """
    us_bank_account: typing.Optional[MandateUsBankAccount] = pydantic.Field(
        alias="us_bank_account", default=None
    )
