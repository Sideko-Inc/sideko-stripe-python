import pydantic
import typing
import typing_extensions

from .address import Address
from .legal_entity_directorship_declaration import LegalEntityDirectorshipDeclaration
from .legal_entity_japan_address import LegalEntityJapanAddress
from .legal_entity_ubo_declaration import LegalEntityUboDeclaration

if typing_extensions.TYPE_CHECKING:
    from .legal_entity_company_verification import LegalEntityCompanyVerification


class LegalEntityCompany(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    address_kana: typing.Optional[LegalEntityJapanAddress] = pydantic.Field(
        alias="address_kana", default=None
    )
    address_kanji: typing.Optional[LegalEntityJapanAddress] = pydantic.Field(
        alias="address_kanji", default=None
    )
    directors_provided: typing.Optional[bool] = pydantic.Field(
        alias="directors_provided", default=None
    )
    """
    Whether the company's directors have been provided. This Boolean will be `true` if you've manually indicated that all directors are provided via [the `directors_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-directors_provided).
    """
    directorship_declaration: typing.Optional[LegalEntityDirectorshipDeclaration] = (
        pydantic.Field(alias="directorship_declaration", default=None)
    )
    executives_provided: typing.Optional[bool] = pydantic.Field(
        alias="executives_provided", default=None
    )
    """
    Whether the company's executives have been provided. This Boolean will be `true` if you've manually indicated that all executives are provided via [the `executives_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided.
    """
    export_license_id: typing.Optional[str] = pydantic.Field(
        alias="export_license_id", default=None
    )
    """
    The export license ID number of the company, also referred as Import Export Code (India only).
    """
    export_purpose_code: typing.Optional[str] = pydantic.Field(
        alias="export_purpose_code", default=None
    )
    """
    The purpose code to use for export transactions (India only).
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The company's legal name. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    name_kana: typing.Optional[str] = pydantic.Field(alias="name_kana", default=None)
    """
    The Kana variation of the company's legal name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    name_kanji: typing.Optional[str] = pydantic.Field(alias="name_kanji", default=None)
    """
    The Kanji variation of the company's legal name (Japan only). Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`.
    """
    owners_provided: typing.Optional[bool] = pydantic.Field(
        alias="owners_provided", default=None
    )
    """
    Whether the company's owners have been provided. This Boolean will be `true` if you've manually indicated that all owners are provided via [the `owners_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together).
    """
    ownership_declaration: typing.Optional[LegalEntityUboDeclaration] = pydantic.Field(
        alias="ownership_declaration", default=None
    )
    ownership_exemption_reason: typing.Optional[
        typing_extensions.Literal[
            "qualified_entity_exceeds_ownership_threshold",
            "qualifies_as_financial_institution",
        ]
    ] = pydantic.Field(alias="ownership_exemption_reason", default=None)
    """
    This value is used to determine if a business is exempt from providing ultimate beneficial owners. See [this support article](https://support.stripe.com/questions/exemption-from-providing-ownership-details) and [changelog](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api) for more details.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The company's phone number (used for verification).
    """
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
    """
    The category identifying the legal structure of the company or legal entity. Also available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details.
    """
    tax_id_provided: typing.Optional[bool] = pydantic.Field(
        alias="tax_id_provided", default=None
    )
    """
    Whether the company's business ID number was provided.
    """
    tax_id_registrar: typing.Optional[str] = pydantic.Field(
        alias="tax_id_registrar", default=None
    )
    """
    The jurisdiction in which the `tax_id` is registered (Germany-based companies only).
    """
    vat_id_provided: typing.Optional[bool] = pydantic.Field(
        alias="vat_id_provided", default=None
    )
    """
    Whether the company's business VAT number was provided.
    """
    verification: typing.Optional["LegalEntityCompanyVerification"] = pydantic.Field(
        alias="verification", default=None
    )
