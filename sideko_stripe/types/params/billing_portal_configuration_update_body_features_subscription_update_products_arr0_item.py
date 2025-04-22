import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item
    """

    prices: typing_extensions.Required[typing.List[str]]

    product: typing_extensions.Required[str]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    prices: typing.List[str] = pydantic.Field(
        alias="prices",
    )
    product: str = pydantic.Field(
        alias="product",
    )
