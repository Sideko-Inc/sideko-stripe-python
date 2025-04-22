import pydantic
import typing

from .account_requirements_alternative import AccountRequirementsAlternative
from .account_requirements_error import AccountRequirementsError


class PersonRequirements(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    alternatives: typing.Optional[typing.List[AccountRequirementsAlternative]] = (
        pydantic.Field(alias="alternatives", default=None)
    )
    """
    Fields that are due and can be satisfied by providing the corresponding alternative fields instead.
    """
    currently_due: typing.List[str] = pydantic.Field(
        alias="currently_due",
    )
    """
    Fields that need to be collected to keep the person's account enabled. If not collected by the account's `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
    """
    errors: typing.List[AccountRequirementsError] = pydantic.Field(
        alias="errors",
    )
    """
    Fields that are `currently_due` and need to be collected again because validation or verification failed.
    """
    eventually_due: typing.List[str] = pydantic.Field(
        alias="eventually_due",
    )
    """
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and the account's `current_deadline` becomes set.
    """
    past_due: typing.List[str] = pydantic.Field(
        alias="past_due",
    )
    """
    Fields that weren't collected by the account's `current_deadline`. These fields need to be collected to enable the person's account.
    """
    pending_verification: typing.List[str] = pydantic.Field(
        alias="pending_verification",
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
