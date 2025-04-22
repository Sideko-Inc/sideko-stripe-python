import pydantic
import typing
import typing_extensions

from .account_requirements_alternative import AccountRequirementsAlternative
from .account_requirements_error import AccountRequirementsError


class AccountCapabilityRequirements(pydantic.BaseModel):
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
    current_deadline: typing.Optional[int] = pydantic.Field(
        alias="current_deadline", default=None
    )
    """
    Date by which the fields in `currently_due` must be collected to keep the capability enabled for the account. These fields may disable the capability sooner if the next threshold is reached before they are collected.
    """
    currently_due: typing.List[str] = pydantic.Field(
        alias="currently_due",
    )
    """
    Fields that need to be collected to keep the capability enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the capability is disabled.
    """
    disabled_reason: typing.Optional[
        typing_extensions.Literal[
            "other",
            "paused.inactivity",
            "pending.onboarding",
            "pending.review",
            "platform_disabled",
            "platform_paused",
            "rejected.inactivity",
            "rejected.other",
            "rejected.unsupported_business",
            "requirements.fields_needed",
        ]
    ] = pydantic.Field(alias="disabled_reason", default=None)
    """
    Description of why the capability is disabled. [Learn more about handling verification issues](https://stripe.com/docs/connect/handling-api-verification).
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
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set.
    """
    past_due: typing.List[str] = pydantic.Field(
        alias="past_due",
    )
    """
    Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the capability on the account.
    """
    pending_verification: typing.List[str] = pydantic.Field(
        alias="pending_verification",
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
