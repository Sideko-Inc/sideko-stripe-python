import pydantic
import typing


class LegalEntityDirectorshipDeclaration(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    """
    The Unix timestamp marking when the directorship declaration attestation was made.
    """
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    """
    The IP address from which the directorship declaration attestation was made.
    """
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
    """
    The user-agent string from the browser where the directorship declaration attestation was made.
    """
