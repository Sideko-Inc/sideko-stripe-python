import pydantic
import typing

from .card_issuing_account_terms_of_service import CardIssuingAccountTermsOfService


class AccountCardIssuingSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[CardIssuingAccountTermsOfService] = pydantic.Field(
        alias="tos_acceptance", default=None
    )
