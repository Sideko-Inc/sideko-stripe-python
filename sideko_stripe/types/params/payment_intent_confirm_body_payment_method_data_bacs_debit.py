import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataBacsDebit(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataBacsDebit
    """

    account_number: typing_extensions.NotRequired[str]

    sort_code: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataBacsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
