import pydantic


class PaymentIntentNextActionCashappQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The date (unix timestamp) when the QR code expires.
    """
    image_url_png: str = pydantic.Field(
        alias="image_url_png",
    )
    """
    The image_url_png string used to render QR code
    """
    image_url_svg: str = pydantic.Field(
        alias="image_url_svg",
    )
    """
    The image_url_svg string used to render QR code
    """
