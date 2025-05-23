import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataBacsDebit(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataBacsDebit
    """

    account_number: typing_extensions.NotRequired[str]

    sort_code: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataBacsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
