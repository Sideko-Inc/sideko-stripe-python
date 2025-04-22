import pydantic
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate
    """

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
