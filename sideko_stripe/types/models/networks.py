import pydantic
import typing


class Networks(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: typing.List[str] = pydantic.Field(
        alias="available",
    )
    """
    All networks available for selection via [payment_method_options.card.network](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
    """
    preferred: typing.Optional[str] = pydantic.Field(alias="preferred", default=None)
    """
    The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.
    """
