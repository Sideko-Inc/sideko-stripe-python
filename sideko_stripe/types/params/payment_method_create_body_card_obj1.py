import pydantic
import typing_extensions


class PaymentMethodCreateBodyCardObj1(typing_extensions.TypedDict):
    """
    PaymentMethodCreateBodyCardObj1
    """

    token: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodyCardObj1(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyCardObj1 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    token: str = pydantic.Field(
        alias="token",
    )
