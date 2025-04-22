import pydantic
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .legal_entity_company_verification_document import (
        LegalEntityCompanyVerificationDocument,
    )


class LegalEntityCompanyVerification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document: "LegalEntityCompanyVerificationDocument" = pydantic.Field(
        alias="document",
    )
