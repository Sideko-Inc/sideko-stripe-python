import pydantic
import typing
import typing_extensions

from .account_create_body_business_profile_annual_revenue import (
    AccountCreateBodyBusinessProfileAnnualRevenue,
    _SerializerAccountCreateBodyBusinessProfileAnnualRevenue,
)
from .account_create_body_business_profile_monthly_estimated_revenue import (
    AccountCreateBodyBusinessProfileMonthlyEstimatedRevenue,
    _SerializerAccountCreateBodyBusinessProfileMonthlyEstimatedRevenue,
)
from .account_create_body_business_profile_support_address import (
    AccountCreateBodyBusinessProfileSupportAddress,
    _SerializerAccountCreateBodyBusinessProfileSupportAddress,
)


class AccountCreateBodyBusinessProfile(typing_extensions.TypedDict):
    """
    Business information about the account.
    """

    annual_revenue: typing_extensions.NotRequired[
        AccountCreateBodyBusinessProfileAnnualRevenue
    ]

    estimated_worker_count: typing_extensions.NotRequired[int]

    mcc: typing_extensions.NotRequired[str]

    monthly_estimated_revenue: typing_extensions.NotRequired[
        AccountCreateBodyBusinessProfileMonthlyEstimatedRevenue
    ]

    name: typing_extensions.NotRequired[str]

    product_description: typing_extensions.NotRequired[str]

    support_address: typing_extensions.NotRequired[
        AccountCreateBodyBusinessProfileSupportAddress
    ]

    support_email: typing_extensions.NotRequired[str]

    support_phone: typing_extensions.NotRequired[str]

    support_url: typing_extensions.NotRequired[typing.Union[str, str]]

    url: typing_extensions.NotRequired[str]


class _SerializerAccountCreateBodyBusinessProfile(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyBusinessProfile handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    annual_revenue: typing.Optional[
        _SerializerAccountCreateBodyBusinessProfileAnnualRevenue
    ] = pydantic.Field(alias="annual_revenue", default=None)
    estimated_worker_count: typing.Optional[int] = pydantic.Field(
        alias="estimated_worker_count", default=None
    )
    mcc: typing.Optional[str] = pydantic.Field(alias="mcc", default=None)
    monthly_estimated_revenue: typing.Optional[
        _SerializerAccountCreateBodyBusinessProfileMonthlyEstimatedRevenue
    ] = pydantic.Field(alias="monthly_estimated_revenue", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    support_address: typing.Optional[
        _SerializerAccountCreateBodyBusinessProfileSupportAddress
    ] = pydantic.Field(alias="support_address", default=None)
    support_email: typing.Optional[str] = pydantic.Field(
        alias="support_email", default=None
    )
    support_phone: typing.Optional[str] = pydantic.Field(
        alias="support_phone", default=None
    )
    support_url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="support_url", default=None
    )
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
