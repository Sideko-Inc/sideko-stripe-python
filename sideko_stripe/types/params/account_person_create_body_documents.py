import pydantic
import typing
import typing_extensions

from .account_person_create_body_documents_company_authorization import (
    AccountPersonCreateBodyDocumentsCompanyAuthorization,
    _SerializerAccountPersonCreateBodyDocumentsCompanyAuthorization,
)
from .account_person_create_body_documents_passport import (
    AccountPersonCreateBodyDocumentsPassport,
    _SerializerAccountPersonCreateBodyDocumentsPassport,
)
from .account_person_create_body_documents_visa import (
    AccountPersonCreateBodyDocumentsVisa,
    _SerializerAccountPersonCreateBodyDocumentsVisa,
)


class AccountPersonCreateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    company_authorization: typing_extensions.NotRequired[
        AccountPersonCreateBodyDocumentsCompanyAuthorization
    ]

    passport: typing_extensions.NotRequired[AccountPersonCreateBodyDocumentsPassport]

    visa: typing_extensions.NotRequired[AccountPersonCreateBodyDocumentsVisa]


class _SerializerAccountPersonCreateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountPersonCreateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    company_authorization: typing.Optional[
        _SerializerAccountPersonCreateBodyDocumentsCompanyAuthorization
    ] = pydantic.Field(alias="company_authorization", default=None)
    passport: typing.Optional[_SerializerAccountPersonCreateBodyDocumentsPassport] = (
        pydantic.Field(alias="passport", default=None)
    )
    visa: typing.Optional[_SerializerAccountPersonCreateBodyDocumentsVisa] = (
        pydantic.Field(alias="visa", default=None)
    )
