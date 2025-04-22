import pydantic
import typing


class PaymentMethodDetailsBlik(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    A unique and immutable identifier assigned by BLIK to every buyer.
    """
