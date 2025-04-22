import pydantic
import typing
import typing_extensions


class PaymentMethodAttachBody(typing_extensions.TypedDict, total=False):
    """
    PaymentMethodAttachBody
    """

    customer: typing_extensions.Required[str]
    """
    The ID of the customer to which to attach the PaymentMethod.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentMethodAttachBody(pydantic.BaseModel):
    """
    Serializer for PaymentMethodAttachBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    customer: str = pydantic.Field(
        alias="customer",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
