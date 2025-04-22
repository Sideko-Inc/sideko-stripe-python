import pydantic
import typing
import typing_extensions

from .issuing_personalization_design_create_body_carrier_text import (
    IssuingPersonalizationDesignCreateBodyCarrierText,
    _SerializerIssuingPersonalizationDesignCreateBodyCarrierText,
)
from .issuing_personalization_design_create_body_metadata import (
    IssuingPersonalizationDesignCreateBodyMetadata,
    _SerializerIssuingPersonalizationDesignCreateBodyMetadata,
)
from .issuing_personalization_design_create_body_preferences import (
    IssuingPersonalizationDesignCreateBodyPreferences,
    _SerializerIssuingPersonalizationDesignCreateBodyPreferences,
)


class IssuingPersonalizationDesignCreateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingPersonalizationDesignCreateBody
    """

    card_logo: typing_extensions.NotRequired[str]
    """
    The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
    """

    carrier_text: typing_extensions.NotRequired[
        IssuingPersonalizationDesignCreateBodyCarrierText
    ]
    """
    Hash containing carrier text, for use with physical bundles that support carrier text.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    lookup_key: typing_extensions.NotRequired[str]
    """
    A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
    """

    metadata: typing_extensions.NotRequired[
        IssuingPersonalizationDesignCreateBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Friendly display name.
    """

    physical_bundle: typing_extensions.Required[str]
    """
    The physical bundle object belonging to this personalization design.
    """

    preferences: typing_extensions.NotRequired[
        IssuingPersonalizationDesignCreateBodyPreferences
    ]
    """
    Information on whether this personalization design is used to create cards when one is not specified.
    """

    transfer_lookup_key: typing_extensions.NotRequired[bool]
    """
    If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design.
    """


class _SerializerIssuingPersonalizationDesignCreateBody(pydantic.BaseModel):
    """
    Serializer for IssuingPersonalizationDesignCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    card_logo: typing.Optional[str] = pydantic.Field(alias="card_logo", default=None)
    carrier_text: typing.Optional[
        _SerializerIssuingPersonalizationDesignCreateBodyCarrierText
    ] = pydantic.Field(alias="carrier_text", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    lookup_key: typing.Optional[str] = pydantic.Field(alias="lookup_key", default=None)
    metadata: typing.Optional[
        _SerializerIssuingPersonalizationDesignCreateBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    physical_bundle: str = pydantic.Field(
        alias="physical_bundle",
    )
    preferences: typing.Optional[
        _SerializerIssuingPersonalizationDesignCreateBodyPreferences
    ] = pydantic.Field(alias="preferences", default=None)
    transfer_lookup_key: typing.Optional[bool] = pydantic.Field(
        alias="transfer_lookup_key", default=None
    )
