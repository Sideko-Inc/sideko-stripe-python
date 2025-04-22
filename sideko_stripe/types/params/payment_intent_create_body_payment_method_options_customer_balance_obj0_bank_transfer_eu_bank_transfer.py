import pydantic
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    """

    country: typing_extensions.Required[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
