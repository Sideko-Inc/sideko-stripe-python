import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    splashscreen: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="splashscreen", default=None
    )
    """
    A File ID representing an image to display on the reader
    """
