import pydantic
import typing


class PaymentIntentNextActionPaynowDisplayQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: str = pydantic.Field(
        alias="data",
    )
    """
    The raw data string used to generate QR code, it should be used together with QR code library.
    """
    hosted_instructions_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_instructions_url", default=None
    )
    """
    The URL to the hosted PayNow instructions page, which allows customers to view the PayNow QR code.
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
