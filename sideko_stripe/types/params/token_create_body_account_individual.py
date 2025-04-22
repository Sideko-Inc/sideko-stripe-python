import pydantic
import typing
import typing_extensions

from .token_create_body_account_individual_address import (
    TokenCreateBodyAccountIndividualAddress,
    _SerializerTokenCreateBodyAccountIndividualAddress,
)
from .token_create_body_account_individual_address_kana import (
    TokenCreateBodyAccountIndividualAddressKana,
    _SerializerTokenCreateBodyAccountIndividualAddressKana,
)
from .token_create_body_account_individual_address_kanji import (
    TokenCreateBodyAccountIndividualAddressKanji,
    _SerializerTokenCreateBodyAccountIndividualAddressKanji,
)
from .token_create_body_account_individual_dob_obj0 import (
    TokenCreateBodyAccountIndividualDobObj0,
    _SerializerTokenCreateBodyAccountIndividualDobObj0,
)
from .token_create_body_account_individual_metadata_obj0 import (
    TokenCreateBodyAccountIndividualMetadataObj0,
    _SerializerTokenCreateBodyAccountIndividualMetadataObj0,
)
from .token_create_body_account_individual_registered_address import (
    TokenCreateBodyAccountIndividualRegisteredAddress,
    _SerializerTokenCreateBodyAccountIndividualRegisteredAddress,
)
from .token_create_body_account_individual_relationship import (
    TokenCreateBodyAccountIndividualRelationship,
    _SerializerTokenCreateBodyAccountIndividualRelationship,
)
from .token_create_body_account_individual_verification import (
    TokenCreateBodyAccountIndividualVerification,
    _SerializerTokenCreateBodyAccountIndividualVerification,
)


class TokenCreateBodyAccountIndividual(typing_extensions.TypedDict):
    """
    TokenCreateBodyAccountIndividual
    """

    address: typing_extensions.NotRequired[TokenCreateBodyAccountIndividualAddress]

    address_kana: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualAddressKana
    ]

    address_kanji: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualAddressKanji
    ]

    dob: typing_extensions.NotRequired[
        typing.Union[TokenCreateBodyAccountIndividualDobObj0, str]
    ]

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
        typing.Union[TokenCreateBodyAccountIndividualMetadataObj0, str]
    ]

    phone: typing_extensions.NotRequired[str]

    political_exposure: typing_extensions.NotRequired[
        typing_extensions.Literal["existing", "none"]
    ]

    registered_address: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualRegisteredAddress
    ]

    relationship: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualRelationship
    ]

    ssn_last_4: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[
        TokenCreateBodyAccountIndividualVerification
    ]


class _SerializerTokenCreateBodyAccountIndividual(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyAccountIndividual handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerTokenCreateBodyAccountIndividualAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    address_kana: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualAddressKana
    ] = pydantic.Field(alias="address_kana", default=None)
    address_kanji: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualAddressKanji
    ] = pydantic.Field(alias="address_kanji", default=None)
    dob: typing.Optional[
        typing.Union[_SerializerTokenCreateBodyAccountIndividualDobObj0, str]
    ] = pydantic.Field(alias="dob", default=None)
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
        typing.Union[_SerializerTokenCreateBodyAccountIndividualMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    political_exposure: typing.Optional[
        typing_extensions.Literal["existing", "none"]
    ] = pydantic.Field(alias="political_exposure", default=None)
    registered_address: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualRegisteredAddress
    ] = pydantic.Field(alias="registered_address", default=None)
    relationship: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualRelationship
    ] = pydantic.Field(alias="relationship", default=None)
    ssn_last_4: typing.Optional[str] = pydantic.Field(alias="ssn_last_4", default=None)
    verification: typing.Optional[
        _SerializerTokenCreateBodyAccountIndividualVerification
    ] = pydantic.Field(alias="verification", default=None)
