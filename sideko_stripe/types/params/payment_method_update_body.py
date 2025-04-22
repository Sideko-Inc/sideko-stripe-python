import pydantic
import typing
import typing_extensions

from .payment_method_update_body_billing_details import (
    PaymentMethodUpdateBodyBillingDetails,
    _SerializerPaymentMethodUpdateBodyBillingDetails,
)
from .payment_method_update_body_card import (
    PaymentMethodUpdateBodyCard,
    _SerializerPaymentMethodUpdateBodyCard,
)
from .payment_method_update_body_metadata_obj0 import (
    PaymentMethodUpdateBodyMetadataObj0,
    _SerializerPaymentMethodUpdateBodyMetadataObj0,
)
from .payment_method_update_body_us_bank_account import (
    PaymentMethodUpdateBodyUsBankAccount,
    _SerializerPaymentMethodUpdateBodyUsBankAccount,
)


class PaymentMethodUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodUpdateBody
    """

    allow_redisplay: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    """

    billing_details: typing_extensions.NotRequired[
        PaymentMethodUpdateBodyBillingDetails
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """

    card: typing_extensions.NotRequired[PaymentMethodUpdateBodyCard]
    """
    If this is a `card` PaymentMethod, this hash contains the user's card details.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    link: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentMethodUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    pay_by_bank: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    """
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    """

    us_bank_account: typing_extensions.NotRequired[PaymentMethodUpdateBodyUsBankAccount]
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """


class _SerializerPaymentMethodUpdateBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
    billing_details: typing.Optional[
        _SerializerPaymentMethodUpdateBodyBillingDetails
    ] = pydantic.Field(alias="billing_details", default=None)
    card: typing.Optional[_SerializerPaymentMethodUpdateBodyCard] = pydantic.Field(
        alias="card", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    link: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="link", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPaymentMethodUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    pay_by_bank: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="pay_by_bank", default=None
    )
    us_bank_account: typing.Optional[
        _SerializerPaymentMethodUpdateBodyUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
