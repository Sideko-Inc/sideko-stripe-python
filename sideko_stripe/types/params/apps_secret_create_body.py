import pydantic
import typing
import typing_extensions

from .apps_secret_create_body_scope import (
    AppsSecretCreateBodyScope,
    _SerializerAppsSecretCreateBodyScope,
)


class AppsSecretCreateBody(typing_extensions.TypedDict, total=False):
    """
    AppsSecretCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    The Unix timestamp for the expiry time of the secret, after which the secret deletes.
    """

    name: typing_extensions.Required[str]
    """
    A name for the secret that's unique within the scope.
    """

    payload: typing_extensions.Required[str]
    """
    The plaintext secret value to be stored.
    """

    scope: typing_extensions.Required[AppsSecretCreateBodyScope]
    """
    Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
    """


class _SerializerAppsSecretCreateBody(pydantic.BaseModel):
    """
    Serializer for AppsSecretCreateBody handling case conversions
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
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    payload: str = pydantic.Field(
        alias="payload",
    )
    scope: _SerializerAppsSecretCreateBodyScope = pydantic.Field(
        alias="scope",
    )
