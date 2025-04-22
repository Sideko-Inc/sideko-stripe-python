import pydantic
import typing
import typing_extensions


class CustomerSubscriptionCreateBodyItemsItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CustomerSubscriptionCreateBodyItemsItemMetadata
    """


class _SerializerCustomerSubscriptionCreateBodyItemsItemMetadata(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyItemsItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
