import pydantic
import typing
import typing_extensions

from .issuing_personalization_design_carrier_text import (
    IssuingPersonalizationDesignCarrierText,
)
from .issuing_personalization_design_metadata import (
    IssuingPersonalizationDesignMetadata,
)
from .issuing_personalization_design_preferences import (
    IssuingPersonalizationDesignPreferences,
)
from .issuing_personalization_design_rejection_reasons import (
    IssuingPersonalizationDesignRejectionReasons,
)
from .issuing_physical_bundle import IssuingPhysicalBundle

if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingPersonalizationDesign(pydantic.BaseModel):
    """
    A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_logo: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="card_logo", default=None
    )
    """
    The file for the card logo to use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
    """
    carrier_text: typing.Optional[IssuingPersonalizationDesignCarrierText] = (
        pydantic.Field(alias="carrier_text", default=None)
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
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
    lookup_key: typing.Optional[str] = pydantic.Field(alias="lookup_key", default=None)
    """
    A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
    """
    metadata: IssuingPersonalizationDesignMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Friendly display name.
    """
    object: typing_extensions.Literal["issuing.personalization_design"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    physical_bundle: typing.Union[str, IssuingPhysicalBundle] = pydantic.Field(
        alias="physical_bundle",
    )
    """
    The physical bundle object belonging to this personalization design.
    """
    preferences: IssuingPersonalizationDesignPreferences = pydantic.Field(
        alias="preferences",
    )
    rejection_reasons: IssuingPersonalizationDesignRejectionReasons = pydantic.Field(
        alias="rejection_reasons",
    )
    status: typing_extensions.Literal["active", "inactive", "rejected", "review"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    Whether this personalization design can be used to create cards.
    """
