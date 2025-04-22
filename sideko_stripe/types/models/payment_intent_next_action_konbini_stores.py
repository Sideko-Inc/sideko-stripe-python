import pydantic
import typing

from .payment_intent_next_action_konbini_familymart import (
    PaymentIntentNextActionKonbiniFamilymart,
)
from .payment_intent_next_action_konbini_lawson import (
    PaymentIntentNextActionKonbiniLawson,
)
from .payment_intent_next_action_konbini_ministop import (
    PaymentIntentNextActionKonbiniMinistop,
)
from .payment_intent_next_action_konbini_seicomart import (
    PaymentIntentNextActionKonbiniSeicomart,
)


class PaymentIntentNextActionKonbiniStores(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    familymart: typing.Optional[PaymentIntentNextActionKonbiniFamilymart] = (
        pydantic.Field(alias="familymart", default=None)
    )
    lawson: typing.Optional[PaymentIntentNextActionKonbiniLawson] = pydantic.Field(
        alias="lawson", default=None
    )
    ministop: typing.Optional[PaymentIntentNextActionKonbiniMinistop] = pydantic.Field(
        alias="ministop", default=None
    )
    seicomart: typing.Optional[PaymentIntentNextActionKonbiniSeicomart] = (
        pydantic.Field(alias="seicomart", default=None)
    )
