import pydantic
import typing

from .account_annual_revenue import AccountAnnualRevenue
from .account_monthly_estimated_revenue import AccountMonthlyEstimatedRevenue
from .address import Address


class AccountBusinessProfile(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    annual_revenue: typing.Optional[AccountAnnualRevenue] = pydantic.Field(
        alias="annual_revenue", default=None
    )
    estimated_worker_count: typing.Optional[int] = pydantic.Field(
        alias="estimated_worker_count", default=None
    )
    """
    An estimated upper bound of employees, contractors, vendors, etc. currently working for the business.
    """
    mcc: typing.Optional[str] = pydantic.Field(alias="mcc", default=None)
    """
    [The merchant category code for the account](/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide.
    """
    monthly_estimated_revenue: typing.Optional[AccountMonthlyEstimatedRevenue] = (
        pydantic.Field(alias="monthly_estimated_revenue", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The customer-facing business name.
    """
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    """
    Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
    """
    support_address: typing.Optional[Address] = pydantic.Field(
        alias="support_address", default=None
    )
    support_email: typing.Optional[str] = pydantic.Field(
        alias="support_email", default=None
    )
    """
    A publicly available email address for sending support issues to.
    """
    support_phone: typing.Optional[str] = pydantic.Field(
        alias="support_phone", default=None
    )
    """
    A publicly available phone number to call with support issues.
    """
    support_url: typing.Optional[str] = pydantic.Field(
        alias="support_url", default=None
    )
    """
    A publicly available website for handling support issues.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The business's publicly available website.
    """
