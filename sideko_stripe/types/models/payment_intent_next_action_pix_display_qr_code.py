import pydantic
import typing


class PaymentIntentNextActionPixDisplayQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[str] = pydantic.Field(alias="data", default=None)
    """
    The raw data string used to generate QR code, it should be used together with QR code library.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The date (unix timestamp) when the PIX expires.
    """
    hosted_instructions_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_instructions_url", default=None
    )
    """
    The URL to the hosted pix instructions page, which allows customers to view the pix QR code.
    """
    image_url_png: typing.Optional[str] = pydantic.Field(
        alias="image_url_png", default=None
    )
    """
    The image_url_png string used to render png QR code
    """
    image_url_svg: typing.Optional[str] = pydantic.Field(
        alias="image_url_svg", default=None
    )
    """
    The image_url_svg string used to render svg QR code
    """
