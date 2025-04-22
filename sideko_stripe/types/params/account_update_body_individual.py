import pydantic
import typing
import typing_extensions

from .account_update_body_individual_address import (
    AccountUpdateBodyIndividualAddress,
    _SerializerAccountUpdateBodyIndividualAddress,
)
from .account_update_body_individual_address_kana import (
    AccountUpdateBodyIndividualAddressKana,
    _SerializerAccountUpdateBodyIndividualAddressKana,
)
from .account_update_body_individual_address_kanji import (
    AccountUpdateBodyIndividualAddressKanji,
    _SerializerAccountUpdateBodyIndividualAddressKanji,
)
from .account_update_body_individual_dob_obj0 import (
    AccountUpdateBodyIndividualDobObj0,
    _SerializerAccountUpdateBodyIndividualDobObj0,
)
from .account_update_body_individual_metadata_obj0 import (
    AccountUpdateBodyIndividualMetadataObj0,
    _SerializerAccountUpdateBodyIndividualMetadataObj0,
)
from .account_update_body_individual_registered_address import (
    AccountUpdateBodyIndividualRegisteredAddress,
    _SerializerAccountUpdateBodyIndividualRegisteredAddress,
)
from .account_update_body_individual_relationship import (
    AccountUpdateBodyIndividualRelationship,
    _SerializerAccountUpdateBodyIndividualRelationship,
)
from .account_update_body_individual_verification import (
    AccountUpdateBodyIndividualVerification,
    _SerializerAccountUpdateBodyIndividualVerification,
)


class AccountUpdateBodyIndividual(typing_extensions.TypedDict):
    """
    Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    address: typing_extensions.NotRequired[AccountUpdateBodyIndividualAddress]

    address_kana: typing_extensions.NotRequired[AccountUpdateBodyIndividualAddressKana]

    address_kanji: typing_extensions.NotRequired[
        AccountUpdateBodyIndividualAddressKanji
    ]

    dob: typing_extensions.NotRequired[
        typing.Union[AccountUpdateBodyIndividualDobObj0, str]
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
        typing.Union[AccountUpdateBodyIndividualMetadataObj0, str]
    ]

    phone: typing_extensions.NotRequired[str]

    political_exposure: typing_extensions.NotRequired[
        typing_extensions.Literal["existing", "none"]
    ]

    registered_address: typing_extensions.NotRequired[
        AccountUpdateBodyIndividualRegisteredAddress
    ]

    relationship: typing_extensions.NotRequired[AccountUpdateBodyIndividualRelationship]

    ssn_last_4: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[AccountUpdateBodyIndividualVerification]


class _SerializerAccountUpdateBodyIndividual(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyIndividual handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerAccountUpdateBodyIndividualAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    address_kana: typing.Optional[_SerializerAccountUpdateBodyIndividualAddressKana] = (
        pydantic.Field(alias="address_kana", default=None)
    )
    address_kanji: typing.Optional[
        _SerializerAccountUpdateBodyIndividualAddressKanji
    ] = pydantic.Field(alias="address_kanji", default=None)
    dob: typing.Optional[
        typing.Union[_SerializerAccountUpdateBodyIndividualDobObj0, str]
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
        typing.Union[_SerializerAccountUpdateBodyIndividualMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    political_exposure: typing.Optional[
        typing_extensions.Literal["existing", "none"]
    ] = pydantic.Field(alias="political_exposure", default=None)
    registered_address: typing.Optional[
        _SerializerAccountUpdateBodyIndividualRegisteredAddress
    ] = pydantic.Field(alias="registered_address", default=None)
    relationship: typing.Optional[
        _SerializerAccountUpdateBodyIndividualRelationship
    ] = pydantic.Field(alias="relationship", default=None)
    ssn_last_4: typing.Optional[str] = pydantic.Field(alias="ssn_last_4", default=None)
    verification: typing.Optional[
        _SerializerAccountUpdateBodyIndividualVerification
    ] = pydantic.Field(alias="verification", default=None)
