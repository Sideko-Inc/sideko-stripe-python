import pydantic
import typing
import typing_extensions

from .account_person_update_body_documents_company_authorization import (
    AccountPersonUpdateBodyDocumentsCompanyAuthorization,
    _SerializerAccountPersonUpdateBodyDocumentsCompanyAuthorization,
)
from .account_person_update_body_documents_passport import (
    AccountPersonUpdateBodyDocumentsPassport,
    _SerializerAccountPersonUpdateBodyDocumentsPassport,
)
from .account_person_update_body_documents_visa import (
    AccountPersonUpdateBodyDocumentsVisa,
    _SerializerAccountPersonUpdateBodyDocumentsVisa,
)


class AccountPersonUpdateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    company_authorization: typing_extensions.NotRequired[
        AccountPersonUpdateBodyDocumentsCompanyAuthorization
    ]

    passport: typing_extensions.NotRequired[AccountPersonUpdateBodyDocumentsPassport]

    visa: typing_extensions.NotRequired[AccountPersonUpdateBodyDocumentsVisa]


class _SerializerAccountPersonUpdateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountPersonUpdateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    company_authorization: typing.Optional[
        _SerializerAccountPersonUpdateBodyDocumentsCompanyAuthorization
    ] = pydantic.Field(alias="company_authorization", default=None)
    passport: typing.Optional[_SerializerAccountPersonUpdateBodyDocumentsPassport] = (
        pydantic.Field(alias="passport", default=None)
    )
    visa: typing.Optional[_SerializerAccountPersonUpdateBodyDocumentsVisa] = (
        pydantic.Field(alias="visa", default=None)
    )
