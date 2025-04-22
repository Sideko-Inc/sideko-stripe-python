import pydantic

from .payment_intent_next_action_swish_qr_code import PaymentIntentNextActionSwishQrCode


class PaymentIntentNextActionSwishHandleRedirectOrDisplayQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hosted_instructions_url: str = pydantic.Field(
        alias="hosted_instructions_url",
    )
    """
    The URL to the hosted Swish instructions page, which allows customers to view the QR code.
    """
    qr_code: PaymentIntentNextActionSwishQrCode = pydantic.Field(
        alias="qr_code",
    )
