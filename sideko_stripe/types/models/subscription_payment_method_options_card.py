import pydantic
import typing
import typing_extensions

from .invoice_mandate_options_card import InvoiceMandateOptionsCard


class SubscriptionPaymentMethodOptionsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mandate_options: typing.Optional[InvoiceMandateOptionsCard] = pydantic.Field(
        alias="mandate_options", default=None
    )
    network: typing.Optional[
        typing_extensions.Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ] = pydantic.Field(alias="network", default=None)
    """
    Selected network to process this Subscription on. Depends on the available networks of the card attached to the Subscription. Can be only set confirm-time.
    """
    request_three_d_secure: typing.Optional[
        typing_extensions.Literal["any", "automatic", "challenge"]
    ] = pydantic.Field(alias="request_three_d_secure", default=None)
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """
