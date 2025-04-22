import pydantic
import typing
import typing_extensions

from .account_update_body_business_profile import (
    AccountUpdateBodyBusinessProfile,
    _SerializerAccountUpdateBodyBusinessProfile,
)
from .account_update_body_capabilities import (
    AccountUpdateBodyCapabilities,
    _SerializerAccountUpdateBodyCapabilities,
)
from .account_update_body_company import (
    AccountUpdateBodyCompany,
    _SerializerAccountUpdateBodyCompany,
)
from .account_update_body_documents import (
    AccountUpdateBodyDocuments,
    _SerializerAccountUpdateBodyDocuments,
)
from .account_update_body_groups import (
    AccountUpdateBodyGroups,
    _SerializerAccountUpdateBodyGroups,
)
from .account_update_body_individual import (
    AccountUpdateBodyIndividual,
    _SerializerAccountUpdateBodyIndividual,
)
from .account_update_body_metadata_obj0 import (
    AccountUpdateBodyMetadataObj0,
    _SerializerAccountUpdateBodyMetadataObj0,
)
from .account_update_body_settings import (
    AccountUpdateBodySettings,
    _SerializerAccountUpdateBodySettings,
)
from .account_update_body_tos_acceptance import (
    AccountUpdateBodyTosAcceptance,
    _SerializerAccountUpdateBodyTosAcceptance,
)


class AccountUpdateBody(typing_extensions.TypedDict, total=False):
    """
    AccountUpdateBody
    """

    account_token: typing_extensions.NotRequired[str]
    """
    An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.
    """

    business_profile: typing_extensions.NotRequired[AccountUpdateBodyBusinessProfile]
    """
    Business information about the account.
    """

    business_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "company", "government_entity", "individual", "non_profit"
        ]
    ]
    """
    The business type. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    capabilities: typing_extensions.NotRequired[AccountUpdateBodyCapabilities]
    """
    Each key of the dictionary represents a capability, and each capability
    maps to its settings (for example, whether it has been requested or not). Each
    capability is inactive until you have provided its specific
    requirements and Stripe has verified them. An account might have some
    of its requested capabilities be active and some be inactive.
    
    Required when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)
    is `none`, which includes Custom accounts.
    """

    company: typing_extensions.NotRequired[AccountUpdateBodyCompany]
    """
    Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    default_currency: typing_extensions.NotRequired[str]
    """
    Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts).
    """

    documents: typing_extensions.NotRequired[AccountUpdateBodyDocuments]
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    email: typing_extensions.NotRequired[str]
    """
    The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn't email the account without your consent.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    external_account: typing_extensions.NotRequired[str]
    """
    A card or bank account to attach to the account for receiving [payouts](/connect/bank-debit-card-payouts) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](/js), or a dictionary, as documented in the `external_account` parameter for [bank account](/api#account_create_bank_account) creation. <br><br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](/api#account_create_bank_account) or [card creation](/api#account_create_card) APIs. After you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    groups: typing_extensions.NotRequired[AccountUpdateBodyGroups]
    """
    A hash of account group type to tokens. These are account groups this account should be added to.
    """

    individual: typing_extensions.NotRequired[AccountUpdateBodyIndividual]
    """
    Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[AccountUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    settings: typing_extensions.NotRequired[AccountUpdateBodySettings]
    """
    Options for customizing how the account functions within Stripe.
    """

    tos_acceptance: typing_extensions.NotRequired[AccountUpdateBodyTosAcceptance]
    """
    Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty.
    """


class _SerializerAccountUpdateBody(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account_token: typing.Optional[str] = pydantic.Field(
        alias="account_token", default=None
    )
    business_profile: typing.Optional[_SerializerAccountUpdateBodyBusinessProfile] = (
        pydantic.Field(alias="business_profile", default=None)
    )
    business_type: typing.Optional[
        typing_extensions.Literal[
            "company", "government_entity", "individual", "non_profit"
        ]
    ] = pydantic.Field(alias="business_type", default=None)
    capabilities: typing.Optional[_SerializerAccountUpdateBodyCapabilities] = (
        pydantic.Field(alias="capabilities", default=None)
    )
    company: typing.Optional[_SerializerAccountUpdateBodyCompany] = pydantic.Field(
        alias="company", default=None
    )
    default_currency: typing.Optional[str] = pydantic.Field(
        alias="default_currency", default=None
    )
    documents: typing.Optional[_SerializerAccountUpdateBodyDocuments] = pydantic.Field(
        alias="documents", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    external_account: typing.Optional[str] = pydantic.Field(
        alias="external_account", default=None
    )
    groups: typing.Optional[_SerializerAccountUpdateBodyGroups] = pydantic.Field(
        alias="groups", default=None
    )
    individual: typing.Optional[_SerializerAccountUpdateBodyIndividual] = (
        pydantic.Field(alias="individual", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerAccountUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    settings: typing.Optional[_SerializerAccountUpdateBodySettings] = pydantic.Field(
        alias="settings", default=None
    )
    tos_acceptance: typing.Optional[_SerializerAccountUpdateBodyTosAcceptance] = (
        pydantic.Field(alias="tos_acceptance", default=None)
    )
