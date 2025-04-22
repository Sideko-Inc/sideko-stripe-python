import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodyShippingOptionsItem(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyShippingOptionsItem
    """

    shipping_rate: typing_extensions.NotRequired[str]


class _SerializerPaymentLinkCreateBodyShippingOptionsItem(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyShippingOptionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
