import pydantic
import typing


class RadarReviewResourceSession(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    browser: typing.Optional[str] = pydantic.Field(alias="browser", default=None)
    """
    The browser used in this browser session (e.g., `Chrome`).
    """
    device: typing.Optional[str] = pydantic.Field(alias="device", default=None)
    """
    Information about the device used for the browser session (e.g., `Samsung SM-G930T`).
    """
    platform: typing.Optional[str] = pydantic.Field(alias="platform", default=None)
    """
    The platform for the browser session (e.g., `Macintosh`).
    """
    version: typing.Optional[str] = pydantic.Field(alias="version", default=None)
    """
    The version for the browser session (e.g., `61.0.3163.100`).
    """
