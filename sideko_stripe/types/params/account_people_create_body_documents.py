import pydantic
import typing
import typing_extensions

from .account_people_create_body_documents_company_authorization import (
    AccountPeopleCreateBodyDocumentsCompanyAuthorization,
    _SerializerAccountPeopleCreateBodyDocumentsCompanyAuthorization,
)
from .account_people_create_body_documents_passport import (
    AccountPeopleCreateBodyDocumentsPassport,
    _SerializerAccountPeopleCreateBodyDocumentsPassport,
)
from .account_people_create_body_documents_visa import (
    AccountPeopleCreateBodyDocumentsVisa,
    _SerializerAccountPeopleCreateBodyDocumentsVisa,
)


class AccountPeopleCreateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    company_authorization: typing_extensions.NotRequired[
        AccountPeopleCreateBodyDocumentsCompanyAuthorization
    ]

    passport: typing_extensions.NotRequired[AccountPeopleCreateBodyDocumentsPassport]

    visa: typing_extensions.NotRequired[AccountPeopleCreateBodyDocumentsVisa]


class _SerializerAccountPeopleCreateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountPeopleCreateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    company_authorization: typing.Optional[
        _SerializerAccountPeopleCreateBodyDocumentsCompanyAuthorization
    ] = pydantic.Field(alias="company_authorization", default=None)
    passport: typing.Optional[_SerializerAccountPeopleCreateBodyDocumentsPassport] = (
        pydantic.Field(alias="passport", default=None)
    )
    visa: typing.Optional[_SerializerAccountPeopleCreateBodyDocumentsVisa] = (
        pydantic.Field(alias="visa", default=None)
    )
