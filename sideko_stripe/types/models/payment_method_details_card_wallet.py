import pydantic
import typing
import typing_extensions

from .payment_method_details_card_wallet_masterpass import (
    PaymentMethodDetailsCardWalletMasterpass,
)
from .payment_method_details_card_wallet_visa_checkout import (
    PaymentMethodDetailsCardWalletVisaCheckout,
)


class PaymentMethodDetailsCardWallet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amex_express_checkout: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="amex_express_checkout", default=None)
    )
    apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="apple_pay", default=None
    )
    dynamic_last4: typing.Optional[str] = pydantic.Field(
        alias="dynamic_last4", default=None
    )
    """
    (For tokenized numbers only.) The last four digits of the device account number.
    """
    google_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="google_pay", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    masterpass: typing.Optional[PaymentMethodDetailsCardWalletMasterpass] = (
        pydantic.Field(alias="masterpass", default=None)
    )
    samsung_pay: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="samsung_pay", default=None
    )
    type_: typing_extensions.Literal[
        "amex_express_checkout",
        "apple_pay",
        "google_pay",
        "link",
        "masterpass",
        "samsung_pay",
        "visa_checkout",
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
    """
    visa_checkout: typing.Optional[PaymentMethodDetailsCardWalletVisaCheckout] = (
        pydantic.Field(alias="visa_checkout", default=None)
    )
