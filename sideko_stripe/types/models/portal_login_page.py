import pydantic
import typing


class PortalLoginPage(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    If `true`, a shareable `url` will be generated that will take your customers to a hosted login page for the customer portal.
    
    If `false`, the previously generated `url`, if any, will be deactivated.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    A shareable URL to the hosted portal login page. Your customers will be able to log in with their [email](https://stripe.com/docs/api/customers/object#customer_object-email) and receive a link to their customer portal.
    """
