import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationUpdateBodyBusinessProfile(typing_extensions.TypedDict):
    """
    The business information shown to customers in the portal.
    """

    headline: typing_extensions.NotRequired[typing.Union[str, str]]

    privacy_policy_url: typing_extensions.NotRequired[typing.Union[str, str]]

    terms_of_service_url: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerBillingPortalConfigurationUpdateBodyBusinessProfile(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyBusinessProfile handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    headline: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="headline", default=None
    )
    privacy_policy_url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="privacy_policy_url", default=None
    )
    terms_of_service_url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="terms_of_service_url", default=None
    )
