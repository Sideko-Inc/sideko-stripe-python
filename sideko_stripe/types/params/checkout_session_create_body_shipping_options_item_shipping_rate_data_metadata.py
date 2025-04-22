import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataMetadata
    """


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
