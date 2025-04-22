import pydantic
import typing
import typing_extensions

from .account_requirements_alternative import AccountRequirementsAlternative
from .account_requirements_error import AccountRequirementsError


class AccountRequirements(pydantic.BaseModel):
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
    Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected.
    """
    currently_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="currently_due", default=None
    )
    """
    Fields that need to be collected to keep the account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
    """
    disabled_reason: typing.Optional[
        typing_extensions.Literal[
            "action_required.requested_capabilities",
            "listed",
            "other",
            "platform_paused",
            "rejected.fraud",
            "rejected.incomplete_verification",
            "rejected.listed",
            "rejected.other",
            "rejected.platform_fraud",
            "rejected.platform_other",
            "rejected.platform_terms_of_service",
            "rejected.terms_of_service",
            "requirements.past_due",
            "requirements.pending_verification",
            "under_review",
        ]
    ] = pydantic.Field(alias="disabled_reason", default=None)
    """
    If the account is disabled, this enum describes why. [Learn more about handling verification issues](https://stripe.com/docs/connect/handling-api-verification).
    """
    errors: typing.Optional[typing.List[AccountRequirementsError]] = pydantic.Field(
        alias="errors", default=None
    )
    """
    Fields that are `currently_due` and need to be collected again because validation or verification failed.
    """
    eventually_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="eventually_due", default=None
    )
    """
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set.
    """
    past_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="past_due", default=None
    )
    """
    Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the account.
    """
    pending_verification: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="pending_verification", default=None
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`. Fields might appear in `eventually_due`, `currently_due`, or `past_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
