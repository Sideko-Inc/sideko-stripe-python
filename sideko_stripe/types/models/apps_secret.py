import pydantic
import typing
import typing_extensions

from .secret_service_resource_scope import SecretServiceResourceScope


class AppsSecret(pydantic.BaseModel):
    """
    Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

    The primary resource in Secret Store is a `secret`. Other apps can't view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

    All Dashboard users and the app backend share `account` scoped secrets. Use the `account` scope for secrets that don't change per-user, like a third-party API key.

    A `user` scoped secret is accessible by the app backend and one specific Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

    Related guide: [Store data between page reloads](https://stripe.com/docs/stripe-apps/store-auth-data-custom-objects)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deleted: typing.Optional[bool] = pydantic.Field(alias="deleted", default=None)
    """
    If true, indicates that this secret has been deleted
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The Unix timestamp for the expiry time of the secret, after which the secret deletes.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    A name for the secret that's unique within the scope.
    """
    object: typing_extensions.Literal["apps.secret"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payload: typing.Optional[str] = pydantic.Field(alias="payload", default=None)
    """
    The plaintext secret value to be stored.
    """
    scope: SecretServiceResourceScope = pydantic.Field(
        alias="scope",
    )
