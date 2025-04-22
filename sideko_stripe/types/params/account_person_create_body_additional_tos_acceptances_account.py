import pydantic
import typing
import typing_extensions


class AccountPersonCreateBodyAdditionalTosAcceptancesAccount(
    typing_extensions.TypedDict
):
    """
    AccountPersonCreateBodyAdditionalTosAcceptancesAccount
    """

    date: typing_extensions.NotRequired[int]

    ip: typing_extensions.NotRequired[str]

    user_agent: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerAccountPersonCreateBodyAdditionalTosAcceptancesAccount(
    pydantic.BaseModel
):
    """
    Serializer for AccountPersonCreateBodyAdditionalTosAcceptancesAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: typing.Optional[int] = pydantic.Field(alias="date", default=None)
    ip: typing.Optional[str] = pydantic.Field(alias="ip", default=None)
    user_agent: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="user_agent", default=None
    )
