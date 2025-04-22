import pydantic
import typing
import typing_extensions

from .token_create_body_person_additional_tos_acceptances import (
    TokenCreateBodyPersonAdditionalTosAcceptances,
    _SerializerTokenCreateBodyPersonAdditionalTosAcceptances,
)
from .token_create_body_person_address import (
    TokenCreateBodyPersonAddress,
    _SerializerTokenCreateBodyPersonAddress,
)
from .token_create_body_person_address_kana import (
    TokenCreateBodyPersonAddressKana,
    _SerializerTokenCreateBodyPersonAddressKana,
)
from .token_create_body_person_address_kanji import (
    TokenCreateBodyPersonAddressKanji,
    _SerializerTokenCreateBodyPersonAddressKanji,
)
from .token_create_body_person_dob_obj0 import (
    TokenCreateBodyPersonDobObj0,
    _SerializerTokenCreateBodyPersonDobObj0,
)
from .token_create_body_person_documents import (
    TokenCreateBodyPersonDocuments,
    _SerializerTokenCreateBodyPersonDocuments,
)
from .token_create_body_person_metadata_obj0 import (
    TokenCreateBodyPersonMetadataObj0,
    _SerializerTokenCreateBodyPersonMetadataObj0,
)
from .token_create_body_person_registered_address import (
    TokenCreateBodyPersonRegisteredAddress,
    _SerializerTokenCreateBodyPersonRegisteredAddress,
)
from .token_create_body_person_relationship import (
    TokenCreateBodyPersonRelationship,
    _SerializerTokenCreateBodyPersonRelationship,
)
from .token_create_body_person_verification import (
    TokenCreateBodyPersonVerification,
    _SerializerTokenCreateBodyPersonVerification,
)


class TokenCreateBodyPerson(typing_extensions.TypedDict):
    """
    Information for the person this token represents.
    """

    additional_tos_acceptances: typing_extensions.NotRequired[
        TokenCreateBodyPersonAdditionalTosAcceptances
    ]

    address: typing_extensions.NotRequired[TokenCreateBodyPersonAddress]

    address_kana: typing_extensions.NotRequired[TokenCreateBodyPersonAddressKana]

    address_kanji: typing_extensions.NotRequired[TokenCreateBodyPersonAddressKanji]

    dob: typing_extensions.NotRequired[typing.Union[TokenCreateBodyPersonDobObj0, str]]

    documents: typing_extensions.NotRequired[TokenCreateBodyPersonDocuments]

    email: typing_extensions.NotRequired[str]

    first_name: typing_extensions.NotRequired[str]

    first_name_kana: typing_extensions.NotRequired[str]

    first_name_kanji: typing_extensions.NotRequired[str]

    full_name_aliases: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]

    gender: typing_extensions.NotRequired[str]

    id_number: typing_extensions.NotRequired[str]

    id_number_secondary: typing_extensions.NotRequired[str]

    last_name: typing_extensions.NotRequired[str]

    last_name_kana: typing_extensions.NotRequired[str]

    last_name_kanji: typing_extensions.NotRequired[str]

    maiden_name: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[TokenCreateBodyPersonMetadataObj0, str]
    ]

    nationality: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]

    political_exposure: typing_extensions.NotRequired[
        typing_extensions.Literal["existing", "none"]
    ]

    registered_address: typing_extensions.NotRequired[
        TokenCreateBodyPersonRegisteredAddress
    ]

    relationship: typing_extensions.NotRequired[TokenCreateBodyPersonRelationship]

    ssn_last_4: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[TokenCreateBodyPersonVerification]


class _SerializerTokenCreateBodyPerson(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPerson handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_tos_acceptances: typing.Optional[
        _SerializerTokenCreateBodyPersonAdditionalTosAcceptances
    ] = pydantic.Field(alias="additional_tos_acceptances", default=None)
    address: typing.Optional[_SerializerTokenCreateBodyPersonAddress] = pydantic.Field(
        alias="address", default=None
    )
    address_kana: typing.Optional[_SerializerTokenCreateBodyPersonAddressKana] = (
        pydantic.Field(alias="address_kana", default=None)
    )
    address_kanji: typing.Optional[_SerializerTokenCreateBodyPersonAddressKanji] = (
        pydantic.Field(alias="address_kanji", default=None)
    )
    dob: typing.Optional[typing.Union[_SerializerTokenCreateBodyPersonDobObj0, str]] = (
        pydantic.Field(alias="dob", default=None)
    )
    documents: typing.Optional[_SerializerTokenCreateBodyPersonDocuments] = (
        pydantic.Field(alias="documents", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
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
        typing.Union[_SerializerTokenCreateBodyPersonMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    nationality: typing.Optional[str] = pydantic.Field(
        alias="nationality", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    political_exposure: typing.Optional[
        typing_extensions.Literal["existing", "none"]
    ] = pydantic.Field(alias="political_exposure", default=None)
    registered_address: typing.Optional[
        _SerializerTokenCreateBodyPersonRegisteredAddress
    ] = pydantic.Field(alias="registered_address", default=None)
    relationship: typing.Optional[_SerializerTokenCreateBodyPersonRelationship] = (
        pydantic.Field(alias="relationship", default=None)
    )
    ssn_last_4: typing.Optional[str] = pydantic.Field(alias="ssn_last_4", default=None)
    verification: typing.Optional[_SerializerTokenCreateBodyPersonVerification] = (
        pydantic.Field(alias="verification", default=None)
    )
