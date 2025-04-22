import pydantic
import typing
import typing_extensions

from .setup_attempt_payment_method_details_card import (
    SetupAttemptPaymentMethodDetailsCard,
)
from .setup_attempt_payment_method_details_naver_pay import (
    SetupAttemptPaymentMethodDetailsNaverPay,
)

if typing_extensions.TYPE_CHECKING:
    from .setup_attempt_payment_method_details_bancontact import (
        SetupAttemptPaymentMethodDetailsBancontact,
    )
    from .setup_attempt_payment_method_details_card_present import (
        SetupAttemptPaymentMethodDetailsCardPresent,
    )
    from .setup_attempt_payment_method_details_ideal import (
        SetupAttemptPaymentMethodDetailsIdeal,
    )
    from .setup_attempt_payment_method_details_sofort import (
        SetupAttemptPaymentMethodDetailsSofort,
    )


class SetupAttemptPaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="acss_debit", default=None
    )
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    au_becs_debit: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="au_becs_debit", default=None
    )
    bacs_debit: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="bacs_debit", default=None
    )
    bancontact: typing.Optional["SetupAttemptPaymentMethodDetailsBancontact"] = (
        pydantic.Field(alias="bancontact", default=None)
    )
    boleto: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="boleto", default=None
    )
    card: typing.Optional[SetupAttemptPaymentMethodDetailsCard] = pydantic.Field(
        alias="card", default=None
    )
    card_present: typing.Optional["SetupAttemptPaymentMethodDetailsCardPresent"] = (
        pydantic.Field(alias="card_present", default=None)
    )
    cashapp: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="cashapp", default=None
    )
    ideal: typing.Optional["SetupAttemptPaymentMethodDetailsIdeal"] = pydantic.Field(
        alias="ideal", default=None
    )
    kakao_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kakao_pay", default=None
    )
    klarna: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="klarna", default=None
    )
    kr_card: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="kr_card", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    naver_pay: typing.Optional[SetupAttemptPaymentMethodDetailsNaverPay] = (
        pydantic.Field(alias="naver_pay", default=None)
    )
    nz_bank_account: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="nz_bank_account", default=None
    )
    paypal: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="paypal", default=None
    )
    revolut_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="revolut_pay", default=None
    )
    sepa_debit: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="sepa_debit", default=None
    )
    sofort: typing.Optional["SetupAttemptPaymentMethodDetailsSofort"] = pydantic.Field(
        alias="sofort", default=None
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of the payment method used in the SetupIntent (e.g., `card`). An additional hash is included on `payment_method_details` with a name matching this value. It contains confirmation-specific information for the payment method.
    """
    us_bank_account: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="us_bank_account", default=None
    )
