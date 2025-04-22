import pydantic

from .payment_links_resource_completed_sessions import (
    PaymentLinksResourceCompletedSessions,
)


class PaymentLinksResourceRestrictions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    completed_sessions: PaymentLinksResourceCompletedSessions = pydantic.Field(
        alias="completed_sessions",
    )
