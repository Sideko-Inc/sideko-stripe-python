import pydantic
import typing
import typing_extensions

from .test_helper_treasury_received_credit_create_body_initiating_payment_method_details import (
    TestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetails,
    _SerializerTestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetails,
)


class TestHelperTreasuryReceivedCreditCreateBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryReceivedCreditCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    Amount (in cents) to be transferred.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_account: typing_extensions.Required[str]
    """
    The FinancialAccount to send funds to.
    """

    initiating_payment_method_details: typing_extensions.NotRequired[
        TestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetails
    ]
    """
    Initiating payment method details for the object.
    """

    network: typing_extensions.Required[
        typing_extensions.Literal["ach", "us_domestic_wire"]
    ]
    """
    Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type.
    """


class _SerializerTestHelperTreasuryReceivedCreditCreateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryReceivedCreditCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    initiating_payment_method_details: typing.Optional[
        _SerializerTestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetails
    ] = pydantic.Field(alias="initiating_payment_method_details", default=None)
    network: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="network",
    )
