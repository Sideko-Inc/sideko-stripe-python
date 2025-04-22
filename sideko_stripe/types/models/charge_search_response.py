import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .charge import Charge


class ChargeSearchResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List["Charge"] = pydantic.Field(
        alias="data",
    )
    has_more: bool = pydantic.Field(
        alias="has_more",
    )
    next_page: typing.Optional[str] = pydantic.Field(alias="next_page", default=None)
    object: typing_extensions.Literal["search_result"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    total_count: typing.Optional[int] = pydantic.Field(
        alias="total_count", default=None
    )
    """
    The total number of objects that match the query, only accurate up to 10,000.
    """
    url: str = pydantic.Field(
        alias="url",
    )
