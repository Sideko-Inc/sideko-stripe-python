import pydantic
import typing
import typing_extensions


class PaymentIntentApplyCustomerBalanceBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentApplyCustomerBalanceBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Amount that you intend to apply to this PaymentIntent from the customer’s cash balance. If the PaymentIntent was created by an Invoice, the full amount of the PaymentIntent is applied regardless of this parameter.
    
    A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency). The maximum amount is the amount of the PaymentIntent.
    
    When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentIntentApplyCustomerBalanceBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentApplyCustomerBalanceBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
