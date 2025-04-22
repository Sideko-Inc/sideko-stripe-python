import pydantic
import typing

from .setup_intent_payment_method_options_acss_debit1 import (
    SetupIntentPaymentMethodOptionsAcssDebit1,
)
from .setup_intent_payment_method_options_bacs_debit1 import (
    SetupIntentPaymentMethodOptionsBacsDebit1,
)
from .setup_intent_payment_method_options_card1 import (
    SetupIntentPaymentMethodOptionsCard1,
)
from .setup_intent_payment_method_options_paypal1 import (
    SetupIntentPaymentMethodOptionsPaypal1,
)
from .setup_intent_payment_method_options_sepa_debit1 import (
    SetupIntentPaymentMethodOptionsSepaDebit1,
)
from .setup_intent_payment_method_options_us_bank_account1 import (
    SetupIntentPaymentMethodOptionsUsBankAccount1,
)
from .setup_intent_type_specific_payment_method_options_client import (
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
)


class SetupIntentPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acss_debit: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsAcssDebit1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="acss_debit", default=None)
    amazon_pay: typing.Optional[
        typing.Union[
            typing.Dict[str, typing.Any],
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="amazon_pay", default=None)
    bacs_debit: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsBacsDebit1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="bacs_debit", default=None)
    card: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsCard1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="card", default=None)
    card_present: typing.Optional[
        typing.Union[
            typing.Dict[str, typing.Any],
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="card_present", default=None)
    link: typing.Optional[
        typing.Union[
            typing.Dict[str, typing.Any],
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="link", default=None)
    paypal: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsPaypal1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="paypal", default=None)
    sepa_debit: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsSepaDebit1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="sepa_debit", default=None)
    us_bank_account: typing.Optional[
        typing.Union[
            SetupIntentPaymentMethodOptionsUsBankAccount1,
            SetupIntentTypeSpecificPaymentMethodOptionsClient,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
