import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_acss_debit import (
    SetupIntentConfirmBodyPaymentMethodOptionsAcssDebit,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsAcssDebit,
)
from .setup_intent_confirm_body_payment_method_options_bacs_debit import (
    SetupIntentConfirmBodyPaymentMethodOptionsBacsDebit,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsBacsDebit,
)
from .setup_intent_confirm_body_payment_method_options_card import (
    SetupIntentConfirmBodyPaymentMethodOptionsCard,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsCard,
)
from .setup_intent_confirm_body_payment_method_options_paypal import (
    SetupIntentConfirmBodyPaymentMethodOptionsPaypal,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsPaypal,
)
from .setup_intent_confirm_body_payment_method_options_sepa_debit import (
    SetupIntentConfirmBodyPaymentMethodOptionsSepaDebit,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsSepaDebit,
)
from .setup_intent_confirm_body_payment_method_options_us_bank_account import (
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount,
)


class SetupIntentConfirmBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment method-specific configuration for this SetupIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsAcssDebit
    ]

    amazon_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    bacs_debit: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsBacsDebit
    ]

    card: typing_extensions.NotRequired[SetupIntentConfirmBodyPaymentMethodOptionsCard]

    card_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paypal: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsPaypal
    ]

    sepa_debit: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsSepaDebit
    ]

    us_bank_account: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    bacs_debit: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    card: typing.Optional[_SerializerSetupIntentConfirmBodyPaymentMethodOptionsCard] = (
        pydantic.Field(alias="card", default=None)
    )
    card_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="card_present", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    paypal: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsPaypal
    ] = pydantic.Field(alias="paypal", default=None)
    sepa_debit: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    us_bank_account: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
