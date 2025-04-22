import pydantic
import typing
import typing_extensions

from .treasury_financial_account_create_body_features import (
    TreasuryFinancialAccountCreateBodyFeatures,
    _SerializerTreasuryFinancialAccountCreateBodyFeatures,
)
from .treasury_financial_account_create_body_metadata import (
    TreasuryFinancialAccountCreateBodyMetadata,
    _SerializerTreasuryFinancialAccountCreateBodyMetadata,
)
from .treasury_financial_account_create_body_platform_restrictions import (
    TreasuryFinancialAccountCreateBodyPlatformRestrictions,
    _SerializerTreasuryFinancialAccountCreateBodyPlatformRestrictions,
)


class TreasuryFinancialAccountCreateBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryFinancialAccountCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    features: typing_extensions.NotRequired[TreasuryFinancialAccountCreateBodyFeatures]
    """
    Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.
    """

    metadata: typing_extensions.NotRequired[TreasuryFinancialAccountCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nickname: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The nickname for the FinancialAccount.
    """

    platform_restrictions: typing_extensions.NotRequired[
        TreasuryFinancialAccountCreateBodyPlatformRestrictions
    ]
    """
    The set of functionalities that the platform can restrict on the FinancialAccount.
    """

    supported_currencies: typing_extensions.Required[typing.List[str]]
    """
    The currencies the FinancialAccount can hold a balance in.
    """


class _SerializerTreasuryFinancialAccountCreateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryFinancialAccountCreateBody handling case conversions
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
    features: typing.Optional[_SerializerTreasuryFinancialAccountCreateBodyFeatures] = (
        pydantic.Field(alias="features", default=None)
    )
    metadata: typing.Optional[_SerializerTreasuryFinancialAccountCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    nickname: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="nickname", default=None
    )
    platform_restrictions: typing.Optional[
        _SerializerTreasuryFinancialAccountCreateBodyPlatformRestrictions
    ] = pydantic.Field(alias="platform_restrictions", default=None)
    supported_currencies: typing.List[str] = pydantic.Field(
        alias="supported_currencies",
    )
