import pydantic
import typing
import typing_extensions

from .treasury_financial_account_update_body_features import (
    TreasuryFinancialAccountUpdateBodyFeatures,
    _SerializerTreasuryFinancialAccountUpdateBodyFeatures,
)
from .treasury_financial_account_update_body_forwarding_settings import (
    TreasuryFinancialAccountUpdateBodyForwardingSettings,
    _SerializerTreasuryFinancialAccountUpdateBodyForwardingSettings,
)
from .treasury_financial_account_update_body_metadata import (
    TreasuryFinancialAccountUpdateBodyMetadata,
    _SerializerTreasuryFinancialAccountUpdateBodyMetadata,
)
from .treasury_financial_account_update_body_platform_restrictions import (
    TreasuryFinancialAccountUpdateBodyPlatformRestrictions,
    _SerializerTreasuryFinancialAccountUpdateBodyPlatformRestrictions,
)


class TreasuryFinancialAccountUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryFinancialAccountUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    features: typing_extensions.NotRequired[TreasuryFinancialAccountUpdateBodyFeatures]
    """
    Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field.
    """

    forwarding_settings: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyForwardingSettings
    ]
    """
    A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0
    """

    metadata: typing_extensions.NotRequired[TreasuryFinancialAccountUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nickname: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The nickname for the FinancialAccount.
    """

    platform_restrictions: typing_extensions.NotRequired[
        TreasuryFinancialAccountUpdateBodyPlatformRestrictions
    ]
    """
    The set of functionalities that the platform can restrict on the FinancialAccount.
    """


class _SerializerTreasuryFinancialAccountUpdateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    features: typing.Optional[_SerializerTreasuryFinancialAccountUpdateBodyFeatures] = (
        pydantic.Field(alias="features", default=None)
    )
    forwarding_settings: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyForwardingSettings
    ] = pydantic.Field(alias="forwarding_settings", default=None)
    metadata: typing.Optional[_SerializerTreasuryFinancialAccountUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    nickname: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="nickname", default=None
    )
    platform_restrictions: typing.Optional[
        _SerializerTreasuryFinancialAccountUpdateBodyPlatformRestrictions
    ] = pydantic.Field(alias="platform_restrictions", default=None)
