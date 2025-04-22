import pydantic
import typing
import typing_extensions

from .file_link_metadata import FileLinkMetadata

if typing_extensions.TYPE_CHECKING:
    from .file import File


class FileLink(pydantic.BaseModel):
    """
    To share the contents of a `File` object with non-Stripe users, you can
    create a `FileLink`. `FileLink`s contain a URL that you can use to
    retrieve the contents of the file without authentication.
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
    expired: bool = pydantic.Field(
        alias="expired",
    )
    """
    Returns if the link is already expired.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    Time that the link expires.
    """
    file: typing.Union[str, "File"] = pydantic.Field(
        alias="file",
    )
    """
    The file object this link points to.
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
    metadata: FileLinkMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["file_link"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The publicly accessible URL to download the file.
    """
