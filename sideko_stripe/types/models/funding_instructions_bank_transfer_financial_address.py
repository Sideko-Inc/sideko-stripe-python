import pydantic
import typing
import typing_extensions

from .funding_instructions_bank_transfer_aba_record import (
    FundingInstructionsBankTransferAbaRecord,
)
from .funding_instructions_bank_transfer_iban_record import (
    FundingInstructionsBankTransferIbanRecord,
)
from .funding_instructions_bank_transfer_sort_code_record import (
    FundingInstructionsBankTransferSortCodeRecord,
)
from .funding_instructions_bank_transfer_spei_record import (
    FundingInstructionsBankTransferSpeiRecord,
)
from .funding_instructions_bank_transfer_swift_record import (
    FundingInstructionsBankTransferSwiftRecord,
)
from .funding_instructions_bank_transfer_zengin_record import (
    FundingInstructionsBankTransferZenginRecord,
)


class FundingInstructionsBankTransferFinancialAddress(pydantic.BaseModel):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    aba: typing.Optional[FundingInstructionsBankTransferAbaRecord] = pydantic.Field(
        alias="aba", default=None
    )
    """
    ABA Records contain U.S. bank account details per the ABA format.
    """
    iban: typing.Optional[FundingInstructionsBankTransferIbanRecord] = pydantic.Field(
        alias="iban", default=None
    )
    """
    Iban Records contain E.U. bank account details per the SEPA format.
    """
    sort_code: typing.Optional[FundingInstructionsBankTransferSortCodeRecord] = (
        pydantic.Field(alias="sort_code", default=None)
    )
    """
    Sort Code Records contain U.K. bank account details per the sort code format.
    """
    spei: typing.Optional[FundingInstructionsBankTransferSpeiRecord] = pydantic.Field(
        alias="spei", default=None
    )
    """
    SPEI Records contain Mexico bank account details per the SPEI format.
    """
    supported_networks: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "ach",
                "bacs",
                "domestic_wire_us",
                "fps",
                "sepa",
                "spei",
                "swift",
                "zengin",
            ]
        ]
    ] = pydantic.Field(alias="supported_networks", default=None)
    """
    The payment networks supported by this FinancialAddress
    """
    swift: typing.Optional[FundingInstructionsBankTransferSwiftRecord] = pydantic.Field(
        alias="swift", default=None
    )
    """
    SWIFT Records contain U.S. bank account details per the SWIFT format.
    """
    type_: typing_extensions.Literal[
        "aba", "iban", "sort_code", "spei", "swift", "zengin"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of financial address
    """
    zengin: typing.Optional[FundingInstructionsBankTransferZenginRecord] = (
        pydantic.Field(alias="zengin", default=None)
    )
    """
    Zengin Records contain Japan bank account details per the Zengin format.
    """
