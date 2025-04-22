import pydantic
import typing
import typing_extensions

from .account_people_update_body_documents_company_authorization import (
    AccountPeopleUpdateBodyDocumentsCompanyAuthorization,
    _SerializerAccountPeopleUpdateBodyDocumentsCompanyAuthorization,
)
from .account_people_update_body_documents_passport import (
    AccountPeopleUpdateBodyDocumentsPassport,
    _SerializerAccountPeopleUpdateBodyDocumentsPassport,
)
from .account_people_update_body_documents_visa import (
    AccountPeopleUpdateBodyDocumentsVisa,
    _SerializerAccountPeopleUpdateBodyDocumentsVisa,
)


class AccountPeopleUpdateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    company_authorization: typing_extensions.NotRequired[
        AccountPeopleUpdateBodyDocumentsCompanyAuthorization
    ]

    passport: typing_extensions.NotRequired[AccountPeopleUpdateBodyDocumentsPassport]

    visa: typing_extensions.NotRequired[AccountPeopleUpdateBodyDocumentsVisa]


class _SerializerAccountPeopleUpdateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountPeopleUpdateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    company_authorization: typing.Optional[
        _SerializerAccountPeopleUpdateBodyDocumentsCompanyAuthorization
    ] = pydantic.Field(alias="company_authorization", default=None)
    passport: typing.Optional[_SerializerAccountPeopleUpdateBodyDocumentsPassport] = (
        pydantic.Field(alias="passport", default=None)
    )
    visa: typing.Optional[_SerializerAccountPeopleUpdateBodyDocumentsVisa] = (
        pydantic.Field(alias="visa", default=None)
    )
