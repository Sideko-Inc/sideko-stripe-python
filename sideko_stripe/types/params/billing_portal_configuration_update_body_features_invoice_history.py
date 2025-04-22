import pydantic
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory
    """

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
