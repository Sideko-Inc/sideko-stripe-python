import pydantic
import typing


class AccountTermsOfService(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    """
    The Unix timestamp marking when the account representative accepted the service agreement.
    """
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    """
    The IP address from which the account representative accepted the service agreement.
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The user agent of the browser from which the account representative accepted the service agreement.
    """
