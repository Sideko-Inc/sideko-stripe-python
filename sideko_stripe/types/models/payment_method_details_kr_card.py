import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsKrCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: typing.Optional[
        typing_extensions.Literal[
            "bc",
            "citi",
            "hana",
            "hyundai",
            "jeju",
            "jeonbuk",
            "kakaobank",
            "kbank",
            "kdbbank",
            "kookmin",
            "kwangju",
            "lotte",
            "mg",
            "nh",
            "post",
            "samsung",
            "savingsbank",
            "shinhan",
            "shinhyup",
            "suhyup",
            "tossbank",
            "woori",
        ]
    ] = pydantic.Field(alias="brand", default=None)
    """
    The local credit or debit card brand.
    """
    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    A unique identifier for the buyer as determined by the local payment processor.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the card. This may not be present for American Express cards.
    """
