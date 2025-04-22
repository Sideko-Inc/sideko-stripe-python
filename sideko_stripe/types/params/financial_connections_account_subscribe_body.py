import pydantic
import typing
import typing_extensions


class FinancialConnectionsAccountSubscribeBody(
    typing_extensions.TypedDict, total=False
):
    """
    FinancialConnectionsAccountSubscribeBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    features: typing_extensions.Required[
        typing.List[typing_extensions.Literal["transactions"]]
    ]
    """
    The list of account features to which you would like to subscribe.
    """


class _SerializerFinancialConnectionsAccountSubscribeBody(pydantic.BaseModel):
    """
    Serializer for FinancialConnectionsAccountSubscribeBody handling case conversions
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
    features: typing.List[typing_extensions.Literal["transactions"]] = pydantic.Field(
        alias="features",
    )
