import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_acss_debit import (
    SetupIntentUpdateBodyPaymentMethodOptionsAcssDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsAcssDebit,
)
from .setup_intent_update_body_payment_method_options_bacs_debit import (
    SetupIntentUpdateBodyPaymentMethodOptionsBacsDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsBacsDebit,
)
from .setup_intent_update_body_payment_method_options_card import (
    SetupIntentUpdateBodyPaymentMethodOptionsCard,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsCard,
)
from .setup_intent_update_body_payment_method_options_paypal import (
    SetupIntentUpdateBodyPaymentMethodOptionsPaypal,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsPaypal,
)
from .setup_intent_update_body_payment_method_options_sepa_debit import (
    SetupIntentUpdateBodyPaymentMethodOptionsSepaDebit,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebit,
)
from .setup_intent_update_body_payment_method_options_us_bank_account import (
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount,
)


class SetupIntentUpdateBodyPaymentMethodOptions(typing_extensions.TypedDict):
    """
    Payment method-specific configuration for this SetupIntent.
    """

    acss_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsAcssDebit
    ]

    amazon_pay: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    bacs_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsBacsDebit
    ]

    card: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodOptionsCard]

    card_present: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]

    paypal: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsPaypal
    ]

    sepa_debit: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsSepaDebit
    ]

    us_bank_account: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptions(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsAcssDebit
    ] = pydantic.Field(alias="acss_debit", default=None)
    amazon_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    bacs_debit: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsBacsDebit
    ] = pydantic.Field(alias="bacs_debit", default=None)
    card: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodOptionsCard] = (
        pydantic.Field(alias="card", default=None)
    )
    card_present: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="card_present", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    paypal: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsPaypal
    ] = pydantic.Field(alias="paypal", default=None)
    sepa_debit: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebit
    ] = pydantic.Field(alias="sepa_debit", default=None)
    us_bank_account: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
