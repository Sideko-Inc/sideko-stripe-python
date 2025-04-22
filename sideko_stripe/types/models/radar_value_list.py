import pydantic
import typing_extensions

from .radar_value_list_list_items import RadarValueListListItems
from .radar_value_list_metadata import RadarValueListMetadata


class RadarValueList(pydantic.BaseModel):
    """
    Value lists allow you to group values together which can then be referenced in rules.

    Related guide: [Default Stripe lists](https://stripe.com/docs/radar/lists#managing-list-items)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    alias: str = pydantic.Field(
        alias="alias",
    )
    """
    The name of the value list for use in rules.
    """
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
    The name or email address of the user who created this value list.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    item_type: typing_extensions.Literal[
        "card_bin",
        "card_fingerprint",
        "case_sensitive_string",
        "country",
        "customer_id",
        "email",
        "ip_address",
        "sepa_debit_fingerprint",
        "string",
        "us_bank_account_fingerprint",
    ] = pydantic.Field(
        alias="item_type",
    )
    """
    The type of items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`.
    """
    list_items: RadarValueListListItems = pydantic.Field(
        alias="list_items",
    )
    """
    List of items contained within this value list.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: RadarValueListMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the value list.
    """
    object: typing_extensions.Literal["radar.value_list"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
