import pydantic
import typing


class PersonRelationship(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorizer: typing.Optional[bool] = pydantic.Field(alias="authorizer", default=None)
    """
    Whether the person is the authorizer of the account's representative.
    """
    director: typing.Optional[bool] = pydantic.Field(alias="director", default=None)
    """
    Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
    """
    executive: typing.Optional[bool] = pydantic.Field(alias="executive", default=None)
    """
    Whether the person has significant responsibility to control, manage, or direct the organization.
    """
    legal_guardian: typing.Optional[bool] = pydantic.Field(
        alias="legal_guardian", default=None
    )
    """
    Whether the person is the legal guardian of the account's representative.
    """
    owner: typing.Optional[bool] = pydantic.Field(alias="owner", default=None)
    """
    Whether the person is an owner of the account’s legal entity.
    """
    percent_ownership: typing.Optional[float] = pydantic.Field(
        alias="percent_ownership", default=None
    )
    """
    The percent owned by the person of the account's legal entity.
    """
    representative: typing.Optional[bool] = pydantic.Field(
        alias="representative", default=None
    )
    """
    Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
    """
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    """
    The person's title (e.g., CEO, Support Engineer).
    """
