import pydantic
import typing
import typing_extensions


class AccountUpdateBodyIndividualRelationship(typing_extensions.TypedDict):
    """
    AccountUpdateBodyIndividualRelationship
    """

    director: typing_extensions.NotRequired[bool]

    executive: typing_extensions.NotRequired[bool]

    owner: typing_extensions.NotRequired[bool]

    percent_ownership: typing_extensions.NotRequired[typing.Union[float, str]]

    title: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateBodyIndividualRelationship(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyIndividualRelationship handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    director: typing.Optional[bool] = pydantic.Field(alias="director", default=None)
    executive: typing.Optional[bool] = pydantic.Field(alias="executive", default=None)
    owner: typing.Optional[bool] = pydantic.Field(alias="owner", default=None)
    percent_ownership: typing.Optional[typing.Union[float, str]] = pydantic.Field(
        alias="percent_ownership", default=None
    )
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
