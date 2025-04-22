import pydantic
import typing
import typing_extensions


class PaymentMethodNaverPay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.
    """
    funding: typing_extensions.Literal["card", "points"] = pydantic.Field(
        alias="funding",
    )
    """
    Whether to fund this transaction with Naver Pay points or a card.
    """
