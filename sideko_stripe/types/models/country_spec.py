import pydantic
import typing
import typing_extensions

from .country_spec_supported_bank_account_currencies import (
    CountrySpecSupportedBankAccountCurrencies,
)
from .country_spec_verification_fields import CountrySpecVerificationFields


class CountrySpec(pydantic.BaseModel):
    """
    Stripe needs to collect certain pieces of information about each account
    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](/docs/connect/required-verification-information).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_currency: str = pydantic.Field(
        alias="default_currency",
    )
    """
    The default currency for this country. This applies to both payment methods and bank accounts.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object. Represented as the ISO country code for this country.
    """
    object: typing_extensions.Literal["country_spec"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    supported_bank_account_currencies: CountrySpecSupportedBankAccountCurrencies = (
        pydantic.Field(
            alias="supported_bank_account_currencies",
        )
    )
    """
    Currencies that can be accepted in the specific country (for transfers).
    """
    supported_payment_currencies: typing.List[str] = pydantic.Field(
        alias="supported_payment_currencies",
    )
    """
    Currencies that can be accepted in the specified country (for payments).
    """
    supported_payment_methods: typing.List[str] = pydantic.Field(
        alias="supported_payment_methods",
    )
    """
    Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges).
    """
    supported_transfer_countries: typing.List[str] = pydantic.Field(
        alias="supported_transfer_countries",
    )
    """
    Countries that can accept transfers from the specified country.
    """
    verification_fields: CountrySpecVerificationFields = pydantic.Field(
        alias="verification_fields",
    )
