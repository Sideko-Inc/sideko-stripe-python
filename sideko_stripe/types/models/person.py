import pydantic
import typing
import typing_extensions

from .address import Address
from .legal_entity_dob import LegalEntityDob
from .legal_entity_japan_address import LegalEntityJapanAddress
from .person_additional_tos_acceptances import PersonAdditionalTosAcceptances
from .person_future_requirements import PersonFutureRequirements
from .person_metadata import PersonMetadata
from .person_relationship import PersonRelationship
from .person_requirements import PersonRequirements

if typing_extensions.TYPE_CHECKING:
    from .legal_entity_person_verification import LegalEntityPersonVerification


class Person(pydantic.BaseModel):
    """
    This is an object representing a person associated with a Stripe account.

    A platform can only access a subset of data in a person for an account where [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, after creating an Account Link or Account Session to start Connect onboarding.

    See the [Standard onboarding](/connect/standard-accounts) or [Express onboarding](/connect/express-accounts) documentation for information about prefilling information and account onboarding steps. Learn more about [handling identity verification with the API](/connect/handling-api-verification#person-information).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: str = pydantic.Field(
        alias="account",
    )
    """
    The account the person is associated with.
    """
    additional_tos_acceptances: typing.Optional[PersonAdditionalTosAcceptances] = (
        pydantic.Field(alias="additional_tos_acceptances", default=None)
    )
    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    address_kana: typing.Optional[LegalEntityJapanAddress] = pydantic.Field(
        alias="address_kana", default=None
    )
    address_kanji: typing.Optional[LegalEntityJapanAddress] = pydantic.Field(
        alias="address_kanji", default=None
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    dob: typing.Optional[LegalEntityDob] = pydantic.Field(alias="dob", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The person's email address. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    The person's first name. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    first_name_kana: typing.Optional[str] = pydantic.Field(
        alias="first_name_kana", default=None
    )
    """
    The Kana variation of the person's first name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    first_name_kanji: typing.Optional[str] = pydantic.Field(
        alias="first_name_kanji", default=None
    )
    """
    The Kanji variation of the person's first name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    full_name_aliases: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="full_name_aliases", default=None
    )
    """
    A list of alternate names or aliases that the person is known by. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    future_requirements: typing.Optional[PersonFutureRequirements] = pydantic.Field(
        alias="future_requirements", default=None
    )
    gender: typing.Optional[str] = pydantic.Field(alias="gender", default=None)
    """
    The person's gender.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    id_number_provided: typing.Optional[bool] = pydantic.Field(
        alias="id_number_provided", default=None
    )
    """
    Whether the person's `id_number` was provided. True if either the full ID number was provided or if only the required part of the ID number was provided (ex. last four of an individual's SSN for the US indicated by `ssn_last_4_provided`).
    """
    id_number_secondary_provided: typing.Optional[bool] = pydantic.Field(
        alias="id_number_secondary_provided", default=None
    )
    """
    Whether the person's `id_number_secondary` was provided.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    The person's last name. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    last_name_kana: typing.Optional[str] = pydantic.Field(
        alias="last_name_kana", default=None
    )
    """
    The Kana variation of the person's last name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    last_name_kanji: typing.Optional[str] = pydantic.Field(
        alias="last_name_kanji", default=None
    )
    """
    The Kanji variation of the person's last name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    maiden_name: typing.Optional[str] = pydantic.Field(
        alias="maiden_name", default=None
    )
    """
    The person's maiden name.
    """
    metadata: typing.Optional[PersonMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationality: typing.Optional[str] = pydantic.Field(
        alias="nationality", default=None
    )
    """
    The country where the person is a national.
    """
    object: typing_extensions.Literal["person"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The person's phone number.
    """
    political_exposure: typing.Optional[
        typing_extensions.Literal["existing", "none"]
    ] = pydantic.Field(alias="political_exposure", default=None)
    """
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    """
    registered_address: typing.Optional[Address] = pydantic.Field(
        alias="registered_address", default=None
    )
    relationship: typing.Optional[PersonRelationship] = pydantic.Field(
        alias="relationship", default=None
    )
    requirements: typing.Optional[PersonRequirements] = pydantic.Field(
        alias="requirements", default=None
    )
    ssn_last_4_provided: typing.Optional[bool] = pydantic.Field(
        alias="ssn_last_4_provided", default=None
    )
    """
    Whether the last four digits of the person's Social Security number have been provided (U.S. only).
    """
    verification: typing.Optional["LegalEntityPersonVerification"] = pydantic.Field(
        alias="verification", default=None
    )
