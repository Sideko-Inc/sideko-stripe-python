import pydantic
import typing_extensions


class AccountLink(pydantic.BaseModel):
    """
    Account Links are the means by which a Connect platform grants a connected account permission to access
    Stripe-hosted applications, such as Connect Onboarding.

    Related guide: [Connect Onboarding](https://stripe.com/docs/connect/custom/hosted-onboarding)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The timestamp at which this account link will expire.
    """
    object: typing_extensions.Literal["account_link"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL for the account link.
    """
