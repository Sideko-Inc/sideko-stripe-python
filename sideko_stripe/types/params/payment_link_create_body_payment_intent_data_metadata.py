import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodyPaymentIntentDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    PaymentLinkCreateBodyPaymentIntentDataMetadata
    """


class _SerializerPaymentLinkCreateBodyPaymentIntentDataMetadata(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyPaymentIntentDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
