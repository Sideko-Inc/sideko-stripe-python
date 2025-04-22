import pydantic
import typing
import typing_extensions

from .token_create_body_person_documents_company_authorization import (
    TokenCreateBodyPersonDocumentsCompanyAuthorization,
    _SerializerTokenCreateBodyPersonDocumentsCompanyAuthorization,
)
from .token_create_body_person_documents_passport import (
    TokenCreateBodyPersonDocumentsPassport,
    _SerializerTokenCreateBodyPersonDocumentsPassport,
)
from .token_create_body_person_documents_visa import (
    TokenCreateBodyPersonDocumentsVisa,
    _SerializerTokenCreateBodyPersonDocumentsVisa,
)


class TokenCreateBodyPersonDocuments(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonDocuments
    """

    company_authorization: typing_extensions.NotRequired[
        TokenCreateBodyPersonDocumentsCompanyAuthorization
    ]

    passport: typing_extensions.NotRequired[TokenCreateBodyPersonDocumentsPassport]

    visa: typing_extensions.NotRequired[TokenCreateBodyPersonDocumentsVisa]


class _SerializerTokenCreateBodyPersonDocuments(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    company_authorization: typing.Optional[
        _SerializerTokenCreateBodyPersonDocumentsCompanyAuthorization
    ] = pydantic.Field(alias="company_authorization", default=None)
    passport: typing.Optional[_SerializerTokenCreateBodyPersonDocumentsPassport] = (
        pydantic.Field(alias="passport", default=None)
    )
    visa: typing.Optional[_SerializerTokenCreateBodyPersonDocumentsVisa] = (
        pydantic.Field(alias="visa", default=None)
    )
