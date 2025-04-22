import pydantic
import typing
import typing_extensions

from .issuing_cardholder_address import IssuingCardholderAddress
from .issuing_cardholder_authorization_controls import (
    IssuingCardholderAuthorizationControls,
)
from .issuing_cardholder_company import IssuingCardholderCompany
from .issuing_cardholder_metadata import IssuingCardholderMetadata
from .issuing_cardholder_requirements import IssuingCardholderRequirements

if typing_extensions.TYPE_CHECKING:
    from .issuing_cardholder_individual import IssuingCardholderIndividual


class IssuingCardholder(pydantic.BaseModel):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

    Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards/virtual/issue-cards#create-cardholder)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing: IssuingCardholderAddress = pydantic.Field(
        alias="billing",
    )
    company: typing.Optional[IssuingCardholderCompany] = pydantic.Field(
        alias="company", default=None
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The cardholder's email address.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    individual: typing.Optional["IssuingCardholderIndividual"] = pydantic.Field(
        alias="individual", default=None
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: IssuingCardholderMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The cardholder's name. This will be printed on cards issued to them.
    """
    object: typing_extensions.Literal["issuing.cardholder"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    """
    The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details.
    """
    preferred_locales: typing.Optional[
        typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
    ] = pydantic.Field(alias="preferred_locales", default=None)
    """
    The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
     This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
    """
    requirements: IssuingCardholderRequirements = pydantic.Field(
        alias="requirements",
    )
    spending_controls: typing.Optional[IssuingCardholderAuthorizationControls] = (
        pydantic.Field(alias="spending_controls", default=None)
    )
    status: typing_extensions.Literal["active", "blocked", "inactive"] = pydantic.Field(
        alias="status",
    )
    """
    Specifies whether to permit authorizations on this cardholder's cards.
    """
    type_: typing_extensions.Literal["company", "individual"] = pydantic.Field(
        alias="type",
    )
    """
    One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details.
    """
