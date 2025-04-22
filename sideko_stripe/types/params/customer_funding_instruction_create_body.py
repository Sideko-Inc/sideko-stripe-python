import pydantic
import typing
import typing_extensions

from .customer_funding_instruction_create_body_bank_transfer import (
    CustomerFundingInstructionCreateBodyBankTransfer,
    _SerializerCustomerFundingInstructionCreateBodyBankTransfer,
)


class CustomerFundingInstructionCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerFundingInstructionCreateBody
    """

    bank_transfer: typing_extensions.Required[
        CustomerFundingInstructionCreateBodyBankTransfer
    ]
    """
    Additional parameters for `bank_transfer` funding types
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    funding_type: typing_extensions.Required[typing_extensions.Literal["bank_transfer"]]
    """
    The `funding_type` to get the instructions for.
    """


class _SerializerCustomerFundingInstructionCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerFundingInstructionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    bank_transfer: _SerializerCustomerFundingInstructionCreateBodyBankTransfer = (
        pydantic.Field(
            alias="bank_transfer",
        )
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    funding_type: typing_extensions.Literal["bank_transfer"] = pydantic.Field(
        alias="funding_type",
    )
