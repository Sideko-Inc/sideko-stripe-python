import pydantic
import typing
import typing_extensions

from .account_requirements_alternative import AccountRequirementsAlternative
from .account_requirements_error import AccountRequirementsError


class AccountFutureRequirements(pydantic.BaseModel):
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
    Date on which `future_requirements` becomes the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on its enablement state prior to transitioning.
    """
    currently_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="currently_due", default=None
    )
    """
    Fields that need to be collected to keep the account enabled. If not collected by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash.
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
    This is typed as an enum for consistency with `requirements.disabled_reason`.
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
    Fields you must collect when all thresholds are reached. As they become required, they appear in `currently_due` as well.
    """
    past_due: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="past_due", default=None
    )
    """
    Fields that weren't collected by `requirements.current_deadline`. These fields need to be collected to enable the capability on the account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`.
    """
    pending_verification: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="pending_verification", default=None
    )
    """
    Fields that might become required depending on the results of verification or review. It's an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`. Fields might appear in `eventually_due` or `currently_due` and in `pending_verification` if verification fails but another verification is still pending.
    """
