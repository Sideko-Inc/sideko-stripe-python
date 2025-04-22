import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_acss_debit import (
    SetupIntentCreateBodyPaymentMethodOptionsAcssDebit,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsAcssDebit,
)
from .setup_intent_create_body_payment_method_options_bacs_debit import (
    SetupIntentCreateBodyPaymentMethodOptionsBacsDebit,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsBacsDebit,
)
from .setup_intent_create_body_payment_method_options_card import (
    SetupIntentCreateBodyPaymentMethodOptionsCard,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsCard,
)
from .setup_intent_create_body_payment_method_options_paypal import (
    SetupIntentCreateBodyPaymentMethodOptionsPaypal,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsPaypal,
)
from .setup_intent_create_body_payment_method_options_sepa_debit import (
    SetupIntentCreateBodyPaymentMethodOptionsSepaDebit,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsSepaDebit,
)
from .setup_intent_create_body_payment_method_options_us_bank_account import (
    SetupIntentCreateBodyPaymentMethodOptionsUsBankAccount,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccount,
)


class SetupIntentCreateBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment method-specific configuration for this SetupIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsAcssDebit
    ]

    amazon_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    bacs_debit: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsBacsDebit
    ]

    card: typing_extensions.NotRequired[SetupIntentCreateBodyPaymentMethodOptionsCard]

    card_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paypal: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsPaypal
    ]

    sepa_debit: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsSepaDebit
    ]

    us_bank_account: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsUsBankAccount
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    bacs_debit: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    card: typing.Optional[_SerializerSetupIntentCreateBodyPaymentMethodOptionsCard] = (
        pydantic.Field(alias="card", default=None)
    )
    card_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="card_present", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    paypal: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsPaypal
    ] = pydantic.Field(alias="paypal", default=None)
    sepa_debit: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    us_bank_account: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
