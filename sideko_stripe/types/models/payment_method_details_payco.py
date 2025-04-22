import pydantic
import typing


class PaymentMethodDetailsPayco(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    A unique identifier for the buyer as determined by the local payment processor.
    """
