import pydantic
import typing
import typing_extensions

from .radar_value_list_create_body_metadata import (
    RadarValueListCreateBodyMetadata,
    _SerializerRadarValueListCreateBodyMetadata,
)


class RadarValueListCreateBody(typing_extensions.TypedDict, total=False):
    """
    RadarValueListCreateBody
    """

    alias: typing_extensions.Required[str]
    """
    The name of the value list for use in rules.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    item_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
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
        ]
    ]
    """
    Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed.
    """

    metadata: typing_extensions.NotRequired[RadarValueListCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.Required[str]
    """
    The human-readable name of the value list.
    """


class _SerializerRadarValueListCreateBody(pydantic.BaseModel):
    """
    Serializer for RadarValueListCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    alias: str = pydantic.Field(
        alias="alias",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    item_type: typing.Optional[
        typing_extensions.Literal[
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
        ]
    ] = pydantic.Field(alias="item_type", default=None)
    metadata: typing.Optional[_SerializerRadarValueListCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
