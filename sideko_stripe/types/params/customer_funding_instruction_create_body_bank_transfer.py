import pydantic
import typing
import typing_extensions

from .customer_funding_instruction_create_body_bank_transfer_eu_bank_transfer import (
    CustomerFundingInstructionCreateBodyBankTransferEuBankTransfer,
    _SerializerCustomerFundingInstructionCreateBodyBankTransferEuBankTransfer,
)


class CustomerFundingInstructionCreateBodyBankTransfer(typing_extensions.TypedDict):
    """
    Additional parameters for `bank_transfer` funding types
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        CustomerFundingInstructionCreateBodyBankTransferEuBankTransfer
    ]

    requested_address_types: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["iban", "sort_code", "spei", "zengin"]]
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


class _SerializerCustomerFundingInstructionCreateBodyBankTransfer(pydantic.BaseModel):
    """
    Serializer for CustomerFundingInstructionCreateBodyBankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerCustomerFundingInstructionCreateBodyBankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    requested_address_types: typing.Optional[
        typing.List[typing_extensions.Literal["iban", "sort_code", "spei", "zengin"]]
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
