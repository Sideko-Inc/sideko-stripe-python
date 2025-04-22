import pydantic
import typing
import typing_extensions

from .account_person_update_body_additional_tos_acceptances import (
    AccountPersonUpdateBodyAdditionalTosAcceptances,
    _SerializerAccountPersonUpdateBodyAdditionalTosAcceptances,
)
from .account_person_update_body_address import (
    AccountPersonUpdateBodyAddress,
    _SerializerAccountPersonUpdateBodyAddress,
)
from .account_person_update_body_address_kana import (
    AccountPersonUpdateBodyAddressKana,
    _SerializerAccountPersonUpdateBodyAddressKana,
)
from .account_person_update_body_address_kanji import (
    AccountPersonUpdateBodyAddressKanji,
    _SerializerAccountPersonUpdateBodyAddressKanji,
)
from .account_person_update_body_dob_obj0 import (
    AccountPersonUpdateBodyDobObj0,
    _SerializerAccountPersonUpdateBodyDobObj0,
)
from .account_person_update_body_documents import (
    AccountPersonUpdateBodyDocuments,
    _SerializerAccountPersonUpdateBodyDocuments,
)
from .account_person_update_body_metadata_obj0 import (
    AccountPersonUpdateBodyMetadataObj0,
    _SerializerAccountPersonUpdateBodyMetadataObj0,
)
from .account_person_update_body_registered_address import (
    AccountPersonUpdateBodyRegisteredAddress,
    _SerializerAccountPersonUpdateBodyRegisteredAddress,
)
from .account_person_update_body_relationship import (
    AccountPersonUpdateBodyRelationship,
    _SerializerAccountPersonUpdateBodyRelationship,
)
from .account_person_update_body_verification import (
    AccountPersonUpdateBodyVerification,
    _SerializerAccountPersonUpdateBodyVerification,
)


class AccountPersonUpdateBody(typing_extensions.TypedDict, total=False):
    """
    AccountPersonUpdateBody
    """

    additional_tos_acceptances: typing_extensions.NotRequired[
        AccountPersonUpdateBodyAdditionalTosAcceptances
    ]
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """

    address: typing_extensions.NotRequired[AccountPersonUpdateBodyAddress]
    """
    The person's address.
    """

    address_kana: typing_extensions.NotRequired[AccountPersonUpdateBodyAddressKana]
    """
    The Kana variation of the person's address (Japan only).
    """

    address_kanji: typing_extensions.NotRequired[AccountPersonUpdateBodyAddressKanji]
    """
    The Kanji variation of the person's address (Japan only).
    """

    dob: typing_extensions.NotRequired[
        typing.Union[AccountPersonUpdateBodyDobObj0, str]
    ]
    """
    The person's date of birth.
    """

    documents: typing_extensions.NotRequired[AccountPersonUpdateBodyDocuments]
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    email: typing_extensions.NotRequired[str]
    """
    The person's email address.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    first_name: typing_extensions.NotRequired[str]
    """
    The person's first name.
    """

    first_name_kana: typing_extensions.NotRequired[str]
    """
    The Kana variation of the person's first name (Japan only).
    """

    first_name_kanji: typing_extensions.NotRequired[str]
    """
    The Kanji variation of the person's first name (Japan only).
    """

    full_name_aliases: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]
    """
    A list of alternate names or aliases that the person is known by.
    """

    gender: typing_extensions.NotRequired[str]
    """
    The person's gender (International regulations require either "male" or "female").
    """

    id_number: typing_extensions.NotRequired[str]
    """
    The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    """

    id_number_secondary: typing_extensions.NotRequired[str]
    """
    The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    """

    last_name: typing_extensions.NotRequired[str]
    """
    The person's last name.
    """

    last_name_kana: typing_extensions.NotRequired[str]
    """
    The Kana variation of the person's last name (Japan only).
    """

    last_name_kanji: typing_extensions.NotRequired[str]
    """
    The Kanji variation of the person's last name (Japan only).
    """

    maiden_name: typing_extensions.NotRequired[str]
    """
    The person's maiden name.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[AccountPersonUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nationality: typing_extensions.NotRequired[str]
    """
    The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    """

    person_token: typing_extensions.NotRequired[str]
    """
    A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    """

    phone: typing_extensions.NotRequired[str]
    """
    The person's phone number.
    """

    political_exposure: typing_extensions.NotRequired[
        typing_extensions.Literal["existing", "none"]
    ]
    """
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    """

    registered_address: typing_extensions.NotRequired[
        AccountPersonUpdateBodyRegisteredAddress
    ]
    """
    The person's registered address.
    """

    relationship: typing_extensions.NotRequired[AccountPersonUpdateBodyRelationship]
    """
    The relationship that this person has with the account's legal entity.
    """

    ssn_last_4: typing_extensions.NotRequired[str]
    """
    The last four digits of the person's Social Security number (U.S. only).
    """

    verification: typing_extensions.NotRequired[AccountPersonUpdateBodyVerification]
    """
    The person's verification status.
    """


class _SerializerAccountPersonUpdateBody(pydantic.BaseModel):
    """
    Serializer for AccountPersonUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    additional_tos_acceptances: typing.Optional[
        _SerializerAccountPersonUpdateBodyAdditionalTosAcceptances
    ] = pydantic.Field(alias="additional_tos_acceptances", default=None)
    address: typing.Optional[_SerializerAccountPersonUpdateBodyAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    address_kana: typing.Optional[_SerializerAccountPersonUpdateBodyAddressKana] = (
        pydantic.Field(alias="address_kana", default=None)
    )
    address_kanji: typing.Optional[_SerializerAccountPersonUpdateBodyAddressKanji] = (
        pydantic.Field(alias="address_kanji", default=None)
    )
    dob: typing.Optional[
        typing.Union[_SerializerAccountPersonUpdateBodyDobObj0, str]
    ] = pydantic.Field(alias="dob", default=None)
    documents: typing.Optional[_SerializerAccountPersonUpdateBodyDocuments] = (
        pydantic.Field(alias="documents", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    first_name_kana: typing.Optional[str] = pydantic.Field(
        alias="first_name_kana", default=None
    )
    first_name_kanji: typing.Optional[str] = pydantic.Field(
        alias="first_name_kanji", default=None
    )
    full_name_aliases: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="full_name_aliases", default=None)
    )
    gender: typing.Optional[str] = pydantic.Field(alias="gender", default=None)
    id_number: typing.Optional[str] = pydantic.Field(alias="id_number", default=None)
    id_number_secondary: typing.Optional[str] = pydantic.Field(
        alias="id_number_secondary", default=None
    )
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    last_name_kana: typing.Optional[str] = pydantic.Field(
        alias="last_name_kana", default=None
    )
    last_name_kanji: typing.Optional[str] = pydantic.Field(
        alias="last_name_kanji", default=None
    )
    maiden_name: typing.Optional[str] = pydantic.Field(
        alias="maiden_name", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerAccountPersonUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    nationality: typing.Optional[str] = pydantic.Field(
        alias="nationality", default=None
    )
    person_token: typing.Optional[str] = pydantic.Field(
        alias="person_token", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    political_exposure: typing.Optional[
        typing_extensions.Literal["existing", "none"]
    ] = pydantic.Field(alias="political_exposure", default=None)
    registered_address: typing.Optional[
        _SerializerAccountPersonUpdateBodyRegisteredAddress
    ] = pydantic.Field(alias="registered_address", default=None)
    relationship: typing.Optional[_SerializerAccountPersonUpdateBodyRelationship] = (
        pydantic.Field(alias="relationship", default=None)
    )
    ssn_last_4: typing.Optional[str] = pydantic.Field(alias="ssn_last_4", default=None)
    verification: typing.Optional[_SerializerAccountPersonUpdateBodyVerification] = (
        pydantic.Field(alias="verification", default=None)
    )
