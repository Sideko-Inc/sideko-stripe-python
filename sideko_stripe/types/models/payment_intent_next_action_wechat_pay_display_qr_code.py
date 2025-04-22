import pydantic


class PaymentIntentNextActionWechatPayDisplayQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: str = pydantic.Field(
        alias="data",
    )
    """
    The data being used to generate QR code
    """
    hosted_instructions_url: str = pydantic.Field(
        alias="hosted_instructions_url",
    )
    """
    The URL to the hosted WeChat Pay instructions page, which allows customers to view the WeChat Pay QR code.
    """
    image_data_url: str = pydantic.Field(
        alias="image_data_url",
    )
    """
    The base64 image data for a pre-generated QR code
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
