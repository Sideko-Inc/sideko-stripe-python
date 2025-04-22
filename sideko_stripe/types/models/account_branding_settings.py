import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class AccountBrandingSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    icon: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="icon", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px.
    """
    logo: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="logo", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px.
    """
    primary_color: typing.Optional[str] = pydantic.Field(
        alias="primary_color", default=None
    )
    """
    A CSS hex color value representing the primary branding color for this account
    """
    secondary_color: typing.Optional[str] = pydantic.Field(
        alias="secondary_color", default=None
    )
    """
    A CSS hex color value representing the secondary branding color for this account
    """
