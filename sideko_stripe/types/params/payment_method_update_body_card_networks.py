import pydantic
import typing
import typing_extensions


class PaymentMethodUpdateBodyCardNetworks(typing_extensions.TypedDict):
    """
    PaymentMethodUpdateBodyCardNetworks
    """

    preferred: typing_extensions.NotRequired[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ]


class _SerializerPaymentMethodUpdateBodyCardNetworks(pydantic.BaseModel):
    """
    Serializer for PaymentMethodUpdateBodyCardNetworks handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred: typing.Optional[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ] = pydantic.Field(alias="preferred", default=None)
