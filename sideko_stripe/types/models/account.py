import pydantic
import typing
import typing_extensions

from .account_business_profile import AccountBusinessProfile
from .account_capabilities import AccountCapabilities
from .account_future_requirements import AccountFutureRequirements
from .account_group_membership import AccountGroupMembership
from .account_metadata import AccountMetadata
from .account_requirements import AccountRequirements
from .account_tos_acceptance import AccountTosAcceptance
from .account_unification_account_controller import AccountUnificationAccountController

if typing_extensions.TYPE_CHECKING:
    from .account_external_accounts import AccountExternalAccounts
    from .account_settings import AccountSettings
    from .legal_entity_company import LegalEntityCompany
    from .person import Person


class Account(pydantic.BaseModel):
    """
    This is an object representing a Stripe account. You can retrieve it to see
    properties on the account like its current requirements or if the account is
    enabled to make live charges or receive payouts.

    For accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts, the properties below are always
    returned.

    For accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`, which includes Standard and Express accounts, some properties are only returned
    until you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions)
    to start Connect Onboarding. Learn about the [differences between accounts](/connect/accounts).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    business_profile: typing.Optional[AccountBusinessProfile] = pydantic.Field(
        alias="business_profile", default=None
    )
    business_type: typing.Optional[
        typing_extensions.Literal[
            "company", "government_entity", "individual", "non_profit"
        ]
    ] = pydantic.Field(alias="business_type", default=None)
    """
    The business type.
    """
    capabilities: typing.Optional[AccountCapabilities] = pydantic.Field(
        alias="capabilities", default=None
    )
    charges_enabled: typing.Optional[bool] = pydantic.Field(
        alias="charges_enabled", default=None
    )
    """
    Whether the account can process charges.
    """
    company: typing.Optional["LegalEntityCompany"] = pydantic.Field(
        alias="company", default=None
    )
    controller: typing.Optional[AccountUnificationAccountController] = pydantic.Field(
        alias="controller", default=None
    )
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    The account's country.
    """
    created: typing.Optional[int] = pydantic.Field(alias="created", default=None)
    """
    Time at which the account was connected. Measured in seconds since the Unix epoch.
    """
    default_currency: typing.Optional[str] = pydantic.Field(
        alias="default_currency", default=None
    )
    """
    Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts).
    """
    details_submitted: typing.Optional[bool] = pydantic.Field(
        alias="details_submitted", default=None
    )
    """
    Whether account details have been submitted. Accounts with Stripe Dashboard access, which includes Standard accounts, cannot receive payouts before this is true. Accounts where this is false should be directed to [an onboarding flow](/connect/onboarding) to finish submitting account details.
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    An email address associated with the account. It's not used for authentication and Stripe doesn't market to this field without explicit approval from the platform.
    """
    external_accounts: typing.Optional["AccountExternalAccounts"] = pydantic.Field(
        alias="external_accounts", default=None
    )
    """
    External accounts (bank accounts and debit cards) currently attached to this account. External accounts are only returned for requests where `controller[is_controller]` is true.
    """
    future_requirements: typing.Optional[AccountFutureRequirements] = pydantic.Field(
        alias="future_requirements", default=None
    )
    groups: typing.Optional[AccountGroupMembership] = pydantic.Field(
        alias="groups", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    individual: typing.Optional["Person"] = pydantic.Field(
        alias="individual", default=None
    )
    """
    This is an object representing a person associated with a Stripe account.
    
    A platform can only access a subset of data in a person for an account where [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, after creating an Account Link or Account Session to start Connect onboarding.
    
    See the [Standard onboarding](/connect/standard-accounts) or [Express onboarding](/connect/express-accounts) documentation for information about prefilling information and account onboarding steps. Learn more about [handling identity verification with the API](/connect/handling-api-verification#person-information).
    """
    metadata: typing.Optional[AccountMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["account"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payouts_enabled: typing.Optional[bool] = pydantic.Field(
        alias="payouts_enabled", default=None
    )
    """
    Whether the funds in this account can be paid out.
    """
    requirements: typing.Optional[AccountRequirements] = pydantic.Field(
        alias="requirements", default=None
    )
    settings: typing.Optional["AccountSettings"] = pydantic.Field(
        alias="settings", default=None
    )
    tos_acceptance: typing.Optional[AccountTosAcceptance] = pydantic.Field(
        alias="tos_acceptance", default=None
    )
    type_: typing.Optional[
        typing_extensions.Literal["custom", "express", "none", "standard"]
    ] = pydantic.Field(alias="type", default=None)
    """
    The Stripe account type. Can be `standard`, `express`, `custom`, or `none`.
    """
