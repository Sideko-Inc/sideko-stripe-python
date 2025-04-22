import pydantic
import typing
import typing_extensions


class AccountPeopleListRelationship(typing_extensions.TypedDict):
    """
    Filters on the list of people returned based on the person's relationship to the account's company.
    """

    authorizer: typing_extensions.NotRequired[bool]

    director: typing_extensions.NotRequired[bool]

    executive: typing_extensions.NotRequired[bool]

    legal_guardian: typing_extensions.NotRequired[bool]

    owner: typing_extensions.NotRequired[bool]

    representative: typing_extensions.NotRequired[bool]


class _SerializerAccountPeopleListRelationship(pydantic.BaseModel):
    """
    Serializer for AccountPeopleListRelationship handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    authorizer: typing.Optional[bool] = pydantic.Field(alias="authorizer", default=None)
    director: typing.Optional[bool] = pydantic.Field(alias="director", default=None)
    executive: typing.Optional[bool] = pydantic.Field(alias="executive", default=None)
    legal_guardian: typing.Optional[bool] = pydantic.Field(
        alias="legal_guardian", default=None
    )
    owner: typing.Optional[bool] = pydantic.Field(alias="owner", default=None)
    representative: typing.Optional[bool] = pydantic.Field(
        alias="representative", default=None
    )
