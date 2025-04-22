import pydantic
import typing
import typing_extensions


class AppsSecretFindScope(typing_extensions.TypedDict):
    """
    Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["account", "user"]]

    user: typing_extensions.NotRequired[str]


class _SerializerAppsSecretFindScope(pydantic.BaseModel):
    """
    Serializer for AppsSecretFindScope handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["account", "user"] = pydantic.Field(
        alias="type",
    )
    user: typing.Optional[str] = pydantic.Field(alias="user", default=None)
