import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyCardObj0Networks(typing_extensions.TypedDict):
    """
    PaymentMethodCreateBodyCardObj0Networks
    """

    preferred: typing_extensions.NotRequired[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ]


class _SerializerPaymentMethodCreateBodyCardObj0Networks(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyCardObj0Networks handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred: typing.Optional[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ] = pydantic.Field(alias="preferred", default=None)
