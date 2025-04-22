import pydantic
import typing_extensions


class RadarValueListItem(pydantic.BaseModel):
    """
    Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

    Related guide: [Managing list items](https://stripe.com/docs/radar/lists#managing-list-items)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: str = pydantic.Field(
        alias="created_by",
    )
    """
    The name or email address of the user who added this item to the value list.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["radar.value_list_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    The value of the item.
    """
    value_list: str = pydantic.Field(
        alias="value_list",
    )
    """
    The identifier of the value list this item belongs to.
    """
