import pydantic
import typing
import typing_extensions


class CustomerSourceVerifyBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSourceVerifyBody
    """

    amounts: typing_extensions.NotRequired[typing.List[int]]
    """
    Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerCustomerSourceVerifyBody(pydantic.BaseModel):
    """
    Serializer for CustomerSourceVerifyBody handling case conversions
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
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
