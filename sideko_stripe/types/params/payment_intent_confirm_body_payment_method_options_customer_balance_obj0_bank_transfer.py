import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_customer_balance_obj0_bank_transfer_eu_bank_transfer import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ]

    requested_address_types: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "aba", "iban", "sepa", "sort_code", "spei", "swift", "zengin"
            ]
        ]
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    requested_address_types: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "aba", "iban", "sepa", "sort_code", "spei", "swift", "zengin"
            ]
        ]
    ] = pydantic.Field(alias="requested_address_types", default=None)
    type_: typing_extensions.Literal[
        "eu_bank_transfer",
        "gb_bank_transfer",
        "jp_bank_transfer",
        "mx_bank_transfer",
        "us_bank_transfer",
    ] = pydantic.Field(
        alias="type",
    )
