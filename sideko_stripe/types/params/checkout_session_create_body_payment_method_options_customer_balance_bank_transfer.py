import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_customer_balance_bank_transfer_eu_bank_transfer import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer
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


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer
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
