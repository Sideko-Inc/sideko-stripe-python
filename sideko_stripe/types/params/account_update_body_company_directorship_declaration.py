import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCompanyDirectorshipDeclaration(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCompanyDirectorshipDeclaration
    """

    date: typing_extensions.NotRequired[int]

    ip: typing_extensions.NotRequired[str]

    user_agent: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateBodyCompanyDirectorshipDeclaration(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCompanyDirectorshipDeclaration handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
