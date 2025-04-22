import pydantic
import typing
import typing_extensions

from .account_requirements_alternative import AccountRequirementsAlternative
from .account_requirements_error import AccountRequirementsError


class AccountCapabilityFutureRequirements(pydantic.BaseModel):
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
    Date on which `future_requirements` becomes the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on the capability's enablement state prior to transitioning.
    """
    currently_due: typing.List[str] = pydantic.Field(
        alias="currently_due",
    )
    """
    Fields that need to be collected to keep the capability enabled. If not collected by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash.
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
    This is typed as an enum for consistency with `requirements.disabled_reason`, but it safe to assume `future_requirements.disabled_reason` is null because fields in `future_requirements` will never disable the account.
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
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well.
    """
    past_due: typing.List[str] = pydantic.Field(
        alias="past_due",
    )
    """
    Fields that weren't collected by `requirements.current_deadline`. These fields need to be collected to enable the capability on the account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`.
    """
    pending_verification: typing.List[str] = pydantic.Field(
        alias="pending_verification",
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`. Fields might appear in `eventually_due` or `currently_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
