import pydantic
import typing
import typing_extensions


class FinancialConnectionsAccountRefreshBody(typing_extensions.TypedDict, total=False):
    """
    FinancialConnectionsAccountRefreshBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    features: typing_extensions.Required[
        typing.List[typing_extensions.Literal["balance", "ownership", "transactions"]]
    ]
    """
    The list of account features that you would like to refresh.
    """


class _SerializerFinancialConnectionsAccountRefreshBody(pydantic.BaseModel):
    """
    Serializer for FinancialConnectionsAccountRefreshBody handling case conversions
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
    features: typing.List[
        typing_extensions.Literal["balance", "ownership", "transactions"]
    ] = pydantic.Field(
        alias="features",
    )
