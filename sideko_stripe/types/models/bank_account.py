import pydantic
import typing
import typing_extensions

from .bank_account_metadata import BankAccountMetadata
from .deleted_customer import DeletedCustomer
from .external_account_requirements import ExternalAccountRequirements

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .customer import Customer


class BankAccount(pydantic.BaseModel):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](/api#external_accounts) are transfer
    destinations on `Account` objects for connected accounts.
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](/payments/bank-debits-transfers)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="account", default=None
    )
    """
    The account this bank account belongs to. Only applicable on Accounts (not customers or recipients) This property is only available when returned as an [External Account](/api/external_account_bank_accounts/object) where [controller.is_controller](/api/accounts/object#account_object-controller-is_controller) is `true`.
    """
    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    """
    The name of the person or business that owns the bank account.
    """
    account_holder_type: typing.Optional[str] = pydantic.Field(
        alias="account_holder_type", default=None
    )
    """
    The type of entity that holds the account. This can be either `individual` or `company`.
    """
    account_type: typing.Optional[str] = pydantic.Field(
        alias="account_type", default=None
    )
    """
    The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    """
    available_payout_methods: typing.Optional[
        typing.List[typing_extensions.Literal["instant", "standard"]]
    ] = pydantic.Field(alias="available_payout_methods", default=None)
    """
    A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.
    """
    bank_name: typing.Optional[str] = pydantic.Field(alias="bank_name", default=None)
    """
    Name of the bank associated with the routing number (e.g., `WELLS FARGO`).
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter ISO code representing the country the bank account is located in.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The ID of the customer that the bank account is associated with.
    """
    default_for_currency: typing.Optional[bool] = pydantic.Field(
        alias="default_for_currency", default=None
    )
    """
    Whether this bank account is the default external account for its currency.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    future_requirements: typing.Optional[ExternalAccountRequirements] = pydantic.Field(
        alias="future_requirements", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    last4: str = pydantic.Field(
        alias="last4",
    )
    """
    The last four digits of the bank account number.
    """
    metadata: typing.Optional[BankAccountMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["bank_account"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requirements: typing.Optional[ExternalAccountRequirements] = pydantic.Field(
        alias="requirements", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
    """
    The routing transit number for the bank account.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a payout sent to this bank account fails, we'll set the status to `errored` and will not continue to send [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the bank details are updated.
    
    For external accounts, possible values are `new`, `errored` and `verification_failed`. If a payout fails, the status is set to `errored` and scheduled payouts are stopped until account details are updated. In the US and India, if we can't [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we'll set the status to `verification_failed`. Other validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply.
    """
