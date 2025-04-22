import pydantic
import typing_extensions


class BillingPortalConfigurationCreateBodyFeaturesInvoiceHistory(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesInvoiceHistory
    """

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesInvoiceHistory(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesInvoiceHistory handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
