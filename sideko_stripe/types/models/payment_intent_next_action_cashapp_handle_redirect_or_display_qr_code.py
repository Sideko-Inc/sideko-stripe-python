import pydantic

from .payment_intent_next_action_cashapp_qr_code import (
    PaymentIntentNextActionCashappQrCode,
)


class PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hosted_instructions_url: str = pydantic.Field(
        alias="hosted_instructions_url",
    )
    """
    The URL to the hosted Cash App Pay instructions page, which allows customers to view the QR code, and supports QR code refreshing on expiration.
    """
    mobile_auth_url: str = pydantic.Field(
        alias="mobile_auth_url",
    )
    """
    The url for mobile redirect based auth
    """
    qr_code: PaymentIntentNextActionCashappQrCode = pydantic.Field(
        alias="qr_code",
    )
