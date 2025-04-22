import pydantic
import typing


class OnlineAcceptance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The customer accepts the mandate from this IP address.
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The customer accepts the mandate using the user agent of the browser.
    """
