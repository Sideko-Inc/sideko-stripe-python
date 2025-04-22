import pydantic
import typing

from .gelato_session_document_options import GelatoSessionDocumentOptions
from .gelato_session_email_options import GelatoSessionEmailOptions
from .gelato_session_phone_options import GelatoSessionPhoneOptions


class GelatoVerificationSessionOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document: typing.Optional[GelatoSessionDocumentOptions] = pydantic.Field(
        alias="document", default=None
    )
    email: typing.Optional[GelatoSessionEmailOptions] = pydantic.Field(
        alias="email", default=None
    )
    id_number: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="id_number", default=None
    )
    phone: typing.Optional[GelatoSessionPhoneOptions] = pydantic.Field(
        alias="phone", default=None
    )
