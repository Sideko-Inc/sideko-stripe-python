import pydantic


class PaymentIntentNextActionPromptpayDisplayQrCode(pydantic.BaseModel):
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
    hosted_instructions_url: str = pydantic.Field(
        alias="hosted_instructions_url",
    )
    """
    The URL to the hosted PromptPay instructions page, which allows customers to view the PromptPay QR code.
    """
    image_url_png: str = pydantic.Field(
        alias="image_url_png",
    )
    """
    The PNG path used to render the QR code, can be used as the source in an HTML img tag
    """
    image_url_svg: str = pydantic.Field(
        alias="image_url_svg",
    )
    """
    The SVG path used to render the QR code, can be used as the source in an HTML img tag
    """
