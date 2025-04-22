import pydantic
import typing
import typing_extensions


class PaymentPagesPrivateCardPaymentMethodOptionsResourceRestrictions(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brands_blocked: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "american_express", "discover_global_network", "mastercard", "visa"
            ]
        ]
    ] = pydantic.Field(alias="brands_blocked", default=None)
    """
    Specify the card brands to block in the Checkout Session. If a customer enters or selects a card belonging to a blocked brand, they can't complete the Session.
    """
