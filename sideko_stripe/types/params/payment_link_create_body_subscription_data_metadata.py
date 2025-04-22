import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodySubscriptionDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    PaymentLinkCreateBodySubscriptionDataMetadata
    """


class _SerializerPaymentLinkCreateBodySubscriptionDataMetadata(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodySubscriptionDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
