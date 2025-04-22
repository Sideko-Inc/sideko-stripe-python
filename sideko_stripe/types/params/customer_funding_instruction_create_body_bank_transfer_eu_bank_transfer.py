import pydantic
import typing_extensions


class CustomerFundingInstructionCreateBodyBankTransferEuBankTransfer(
    typing_extensions.TypedDict
):
    """
    CustomerFundingInstructionCreateBodyBankTransferEuBankTransfer
    """

    country: typing_extensions.Required[str]


class _SerializerCustomerFundingInstructionCreateBodyBankTransferEuBankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for CustomerFundingInstructionCreateBodyBankTransferEuBankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
