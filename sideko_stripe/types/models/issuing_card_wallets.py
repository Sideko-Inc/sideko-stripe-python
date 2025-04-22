import pydantic
import typing

from .issuing_card_apple_pay import IssuingCardApplePay
from .issuing_card_google_pay import IssuingCardGooglePay


class IssuingCardWallets(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apple_pay: IssuingCardApplePay = pydantic.Field(
        alias="apple_pay",
    )
    google_pay: IssuingCardGooglePay = pydantic.Field(
        alias="google_pay",
    )
    primary_account_identifier: typing.Optional[str] = pydantic.Field(
        alias="primary_account_identifier", default=None
    )
    """
    Unique identifier for a card used with digital wallets
    """
