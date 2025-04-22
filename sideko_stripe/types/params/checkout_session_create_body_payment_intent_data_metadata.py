import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentIntentDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodyPaymentIntentDataMetadata
    """


class _SerializerCheckoutSessionCreateBodyPaymentIntentDataMetadata(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentIntentDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
