import pydantic
import typing


class AccountTosAcceptance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    """
    The Unix timestamp marking when the account representative accepted their service agreement
    """
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    """
    The IP address from which the account representative accepted their service agreement
    """
    service_agreement: typing.Optional[str] = pydantic.Field(
        alias="service_agreement", default=None
    )
    """
    The user's service agreement type
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The user agent of the browser from which the account representative accepted their service agreement
    """
