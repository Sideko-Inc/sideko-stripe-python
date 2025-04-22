import pydantic
import typing
import typing_extensions

from .apps_secret_delete_body_scope import (
    AppsSecretDeleteBodyScope,
    _SerializerAppsSecretDeleteBodyScope,
)


class AppsSecretDeleteBody(typing_extensions.TypedDict, total=False):
    """
    AppsSecretDeleteBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    name: typing_extensions.Required[str]
    """
    A name for the secret that's unique within the scope.
    """

    scope: typing_extensions.Required[AppsSecretDeleteBodyScope]
    """
    Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
    """


class _SerializerAppsSecretDeleteBody(pydantic.BaseModel):
    """
    Serializer for AppsSecretDeleteBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    scope: _SerializerAppsSecretDeleteBodyScope = pydantic.Field(
        alias="scope",
    )
