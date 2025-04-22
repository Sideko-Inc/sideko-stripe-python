import pydantic
import typing
import typing_extensions


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata
    """


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
