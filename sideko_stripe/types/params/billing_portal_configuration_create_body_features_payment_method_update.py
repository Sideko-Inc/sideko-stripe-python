import pydantic
import typing_extensions


class BillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate
    """

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
