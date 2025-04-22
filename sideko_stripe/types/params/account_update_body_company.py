import pydantic
import typing
import typing_extensions

from .account_update_body_company_address import (
    AccountUpdateBodyCompanyAddress,
    _SerializerAccountUpdateBodyCompanyAddress,
)
from .account_update_body_company_address_kana import (
    AccountUpdateBodyCompanyAddressKana,
    _SerializerAccountUpdateBodyCompanyAddressKana,
)
from .account_update_body_company_address_kanji import (
    AccountUpdateBodyCompanyAddressKanji,
    _SerializerAccountUpdateBodyCompanyAddressKanji,
)
from .account_update_body_company_directorship_declaration import (
    AccountUpdateBodyCompanyDirectorshipDeclaration,
    _SerializerAccountUpdateBodyCompanyDirectorshipDeclaration,
)
from .account_update_body_company_ownership_declaration import (
    AccountUpdateBodyCompanyOwnershipDeclaration,
    _SerializerAccountUpdateBodyCompanyOwnershipDeclaration,
)
from .account_update_body_company_verification import (
    AccountUpdateBodyCompanyVerification,
    _SerializerAccountUpdateBodyCompanyVerification,
)


class AccountUpdateBodyCompany(typing_extensions.TypedDict):
    """
    Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """

    address: typing_extensions.NotRequired[AccountUpdateBodyCompanyAddress]

    address_kana: typing_extensions.NotRequired[AccountUpdateBodyCompanyAddressKana]

    address_kanji: typing_extensions.NotRequired[AccountUpdateBodyCompanyAddressKanji]

    directors_provided: typing_extensions.NotRequired[bool]

    directorship_declaration: typing_extensions.NotRequired[
        AccountUpdateBodyCompanyDirectorshipDeclaration
    ]

    executives_provided: typing_extensions.NotRequired[bool]

    export_license_id: typing_extensions.NotRequired[str]

    export_purpose_code: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    name_kana: typing_extensions.NotRequired[str]

    name_kanji: typing_extensions.NotRequired[str]

    owners_provided: typing_extensions.NotRequired[bool]

    ownership_declaration: typing_extensions.NotRequired[
        AccountUpdateBodyCompanyOwnershipDeclaration
    ]

    ownership_exemption_reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "qualified_entity_exceeds_ownership_threshold",
            "qualifies_as_financial_institution",
        ]
    ]

    phone: typing_extensions.NotRequired[str]

    registration_number: typing_extensions.NotRequired[str]

    structure: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "free_zone_establishment",
            "free_zone_llc",
            "government_instrumentality",
            "governmental_unit",
            "incorporated_non_profit",
            "incorporated_partnership",
            "limited_liability_partnership",
            "llc",
            "multi_member_llc",
            "private_company",
            "private_corporation",
            "private_partnership",
            "public_company",
            "public_corporation",
            "public_partnership",
            "registered_charity",
            "single_member_llc",
            "sole_establishment",
            "sole_proprietorship",
            "tax_exempt_government_instrumentality",
            "unincorporated_association",
            "unincorporated_non_profit",
            "unincorporated_partnership",
        ]
    ]

    tax_id: typing_extensions.NotRequired[str]

    tax_id_registrar: typing_extensions.NotRequired[str]

    vat_id: typing_extensions.NotRequired[str]

    verification: typing_extensions.NotRequired[AccountUpdateBodyCompanyVerification]


class _SerializerAccountUpdateBodyCompany(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCompany handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerAccountUpdateBodyCompanyAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    address_kana: typing.Optional[_SerializerAccountUpdateBodyCompanyAddressKana] = (
        pydantic.Field(alias="address_kana", default=None)
    )
    address_kanji: typing.Optional[_SerializerAccountUpdateBodyCompanyAddressKanji] = (
        pydantic.Field(alias="address_kanji", default=None)
    )
    directors_provided: typing.Optional[bool] = pydantic.Field(
        alias="directors_provided", default=None
    )
    directorship_declaration: typing.Optional[
        _SerializerAccountUpdateBodyCompanyDirectorshipDeclaration
    ] = pydantic.Field(alias="directorship_declaration", default=None)
    executives_provided: typing.Optional[bool] = pydantic.Field(
        alias="executives_provided", default=None
    )
    export_license_id: typing.Optional[str] = pydantic.Field(
        alias="export_license_id", default=None
    )
    export_purpose_code: typing.Optional[str] = pydantic.Field(
        alias="export_purpose_code", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    name_kana: typing.Optional[str] = pydantic.Field(alias="name_kana", default=None)
    name_kanji: typing.Optional[str] = pydantic.Field(alias="name_kanji", default=None)
    owners_provided: typing.Optional[bool] = pydantic.Field(
        alias="owners_provided", default=None
    )
    ownership_declaration: typing.Optional[
        _SerializerAccountUpdateBodyCompanyOwnershipDeclaration
    ] = pydantic.Field(alias="ownership_declaration", default=None)
    ownership_exemption_reason: typing.Optional[
        typing_extensions.Literal[
            "qualified_entity_exceeds_ownership_threshold",
            "qualifies_as_financial_institution",
        ]
    ] = pydantic.Field(alias="ownership_exemption_reason", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    registration_number: typing.Optional[str] = pydantic.Field(
        alias="registration_number", default=None
    )
    structure: typing.Optional[
        typing_extensions.Literal[
            "free_zone_establishment",
            "free_zone_llc",
            "government_instrumentality",
            "governmental_unit",
            "incorporated_non_profit",
            "incorporated_partnership",
            "limited_liability_partnership",
            "llc",
            "multi_member_llc",
            "private_company",
            "private_corporation",
            "private_partnership",
            "public_company",
            "public_corporation",
            "public_partnership",
            "registered_charity",
            "single_member_llc",
            "sole_establishment",
            "sole_proprietorship",
            "tax_exempt_government_instrumentality",
            "unincorporated_association",
            "unincorporated_non_profit",
            "unincorporated_partnership",
        ]
    ] = pydantic.Field(alias="structure", default=None)
    tax_id: typing.Optional[str] = pydantic.Field(alias="tax_id", default=None)
    tax_id_registrar: typing.Optional[str] = pydantic.Field(
        alias="tax_id_registrar", default=None
    )
    vat_id: typing.Optional[str] = pydantic.Field(alias="vat_id", default=None)
    verification: typing.Optional[_SerializerAccountUpdateBodyCompanyVerification] = (
        pydantic.Field(alias="verification", default=None)
    )
