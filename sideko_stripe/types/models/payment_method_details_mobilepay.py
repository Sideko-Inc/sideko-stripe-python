import pydantic
import typing

from .internal_card import InternalCard


class PaymentMethodDetailsMobilepay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card: typing.Optional[InternalCard] = pydantic.Field(alias="card", default=None)
