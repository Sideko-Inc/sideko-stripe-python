import pydantic
import typing


class PortalBusinessProfile(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    headline: typing.Optional[str] = pydantic.Field(alias="headline", default=None)
    """
    The messaging shown to customers in the portal.
    """
    privacy_policy_url: typing.Optional[str] = pydantic.Field(
        alias="privacy_policy_url", default=None
    )
    """
    A link to the business’s publicly available privacy policy.
    """
    terms_of_service_url: typing.Optional[str] = pydantic.Field(
        alias="terms_of_service_url", default=None
    )
    """
    A link to the business’s publicly available terms of service.
    """
