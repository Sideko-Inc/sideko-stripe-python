import pydantic
import typing

from .payment_method_details_konbini_store import PaymentMethodDetailsKonbiniStore


class PaymentMethodDetailsKonbini(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    store: typing.Optional[PaymentMethodDetailsKonbiniStore] = pydantic.Field(
        alias="store", default=None
    )
