import pydantic
import typing


class IssuingCardholderUserTermsAcceptance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    """
    The Unix timestamp marking when the cardholder accepted the Authorized User Terms.
    """
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    """
    The IP address from which the cardholder accepted the Authorized User Terms.
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The user agent of the browser from which the cardholder accepted the Authorized User Terms.
    """
