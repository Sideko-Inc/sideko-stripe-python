import pydantic
import typing
import typing_extensions


class PaymentMethodDomainUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodDomainUpdateBody
    """

    enabled: typing_extensions.NotRequired[bool]
    """
    Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentMethodDomainUpdateBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodDomainUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
