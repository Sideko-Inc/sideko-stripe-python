import pydantic
import typing

from .account_terms_of_service import AccountTermsOfService


class AccountTreasurySettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tos_acceptance: typing.Optional[AccountTermsOfService] = pydantic.Field(
        alias="tos_acceptance", default=None
    )
