import pydantic
import typing
import typing_extensions


class PaymentIntentVerifyMicrodepositsBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentVerifyMicrodepositsBody
    """

    amounts: typing_extensions.NotRequired[typing.List[int]]
    """
    Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    """

    client_secret: typing_extensions.NotRequired[str]
    """
    The client secret of the PaymentIntent.
    """

    descriptor_code: typing_extensions.NotRequired[str]
    """
    A six-character code starting with SM present in the microdeposit sent to the bank account.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentIntentVerifyMicrodepositsBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentVerifyMicrodepositsBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amounts: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="amounts", default=None
    )
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    descriptor_code: typing.Optional[str] = pydantic.Field(
        alias="descriptor_code", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
