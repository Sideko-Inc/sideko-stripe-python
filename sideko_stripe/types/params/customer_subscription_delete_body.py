import pydantic
import typing
import typing_extensions


class CustomerSubscriptionDeleteBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSubscriptionDeleteBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_now: typing_extensions.NotRequired[bool]
    """
    Can be set to `true` if `at_period_end` is not set to `true`. Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items.
    """

    prorate: typing_extensions.NotRequired[bool]
    """
    Can be set to `true` if `at_period_end` is not set to `true`. Will generate a proration invoice item that credits remaining unused time until the subscription period end.
    """


class _SerializerCustomerSubscriptionDeleteBody(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionDeleteBody handling case conversions
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
    invoice_now: typing.Optional[bool] = pydantic.Field(
        alias="invoice_now", default=None
    )
    prorate: typing.Optional[bool] = pydantic.Field(alias="prorate", default=None)
