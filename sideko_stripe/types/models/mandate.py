import pydantic
import typing
import typing_extensions

from .customer_acceptance import CustomerAcceptance
from .mandate_payment_method_details import MandatePaymentMethodDetails
from .mandate_single_use import MandateSingleUse

if typing_extensions.TYPE_CHECKING:
    from .payment_method import PaymentMethod


class Mandate(pydantic.BaseModel):
    """
    A Mandate is a record of the permission that your customer gives you to debit their payment method.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_acceptance: CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    multi_use: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="multi_use", default=None
    )
    object: typing_extensions.Literal["mandate"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) that the mandate is intended for.
    """
    payment_method: typing.Union[str, "PaymentMethod"] = pydantic.Field(
        alias="payment_method",
    )
    """
    ID of the payment method associated with this mandate.
    """
    payment_method_details: MandatePaymentMethodDetails = pydantic.Field(
        alias="payment_method_details",
    )
    single_use: typing.Optional[MandateSingleUse] = pydantic.Field(
        alias="single_use", default=None
    )
    status: typing_extensions.Literal["active", "inactive", "pending"] = pydantic.Field(
        alias="status",
    )
    """
    The mandate status indicates whether or not you can use it to initiate a payment.
    """
    type_: typing_extensions.Literal["multi_use", "single_use"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the mandate.
    """
