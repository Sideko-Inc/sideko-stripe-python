import pydantic
import typing_extensions


class ForwardingRequestCreateBodyRequestHeadersItem(typing_extensions.TypedDict):
    """
    ForwardingRequestCreateBodyRequestHeadersItem
    """

    name: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerForwardingRequestCreateBodyRequestHeadersItem(pydantic.BaseModel):
    """
    Serializer for ForwardingRequestCreateBodyRequestHeadersItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    value: str = pydantic.Field(
        alias="value",
    )
