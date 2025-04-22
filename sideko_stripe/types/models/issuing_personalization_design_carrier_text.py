import pydantic
import typing


class IssuingPersonalizationDesignCarrierText(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    footer_body: typing.Optional[str] = pydantic.Field(
        alias="footer_body", default=None
    )
    """
    The footer body text of the carrier letter.
    """
    footer_title: typing.Optional[str] = pydantic.Field(
        alias="footer_title", default=None
    )
    """
    The footer title text of the carrier letter.
    """
    header_body: typing.Optional[str] = pydantic.Field(
        alias="header_body", default=None
    )
    """
    The header body text of the carrier letter.
    """
    header_title: typing.Optional[str] = pydantic.Field(
        alias="header_title", default=None
    )
    """
    The header title text of the carrier letter.
    """
