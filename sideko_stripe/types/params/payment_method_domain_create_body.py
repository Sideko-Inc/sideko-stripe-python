import pydantic
import typing
import typing_extensions


class PaymentMethodDomainCreateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodDomainCreateBody
    """

    domain_name: typing_extensions.Required[str]
    """
    The domain name that this payment method domain object represents.
    """

    enabled: typing_extensions.NotRequired[bool]
    """
    Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentMethodDomainCreateBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodDomainCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    domain_name: str = pydantic.Field(
        alias="domain_name",
    )
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
