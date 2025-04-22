import pydantic
import typing

from .account_requirements_error import AccountRequirementsError


class ExternalAccountRequirements(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currently_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="currently_due", default=None
    )
    """
    Fields that need to be collected to keep the external account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
    """
    errors: typing.Optional[typing.List[AccountRequirementsError]] = pydantic.Field(
        alias="errors", default=None
    )
    """
    Fields that are `currently_due` and need to be collected again because validation or verification failed.
    """
    past_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="past_due", default=None
    )
    """
    Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the external account.
    """
    pending_verification: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="pending_verification", default=None
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
