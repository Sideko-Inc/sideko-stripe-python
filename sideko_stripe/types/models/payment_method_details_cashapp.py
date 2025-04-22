import pydantic
import typing


class PaymentMethodDetailsCashapp(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    A unique and immutable identifier assigned by Cash App to every buyer.
    """
    cashtag: typing.Optional[str] = pydantic.Field(alias="cashtag", default=None)
    """
    A public identifier for buyers using Cash App.
    """
