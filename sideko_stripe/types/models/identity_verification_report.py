import pydantic
import typing
import typing_extensions

from .gelato_document_report import GelatoDocumentReport
from .gelato_email_report import GelatoEmailReport
from .gelato_id_number_report import GelatoIdNumberReport
from .gelato_phone_report import GelatoPhoneReport
from .gelato_selfie_report import GelatoSelfieReport
from .gelato_verification_report_options import GelatoVerificationReportOptions


class IdentityVerificationReport(pydantic.BaseModel):
    """
    A VerificationReport is the result of an attempt to collect and verify data from a user.
    The collection of verification checks performed is determined from the `type` and `options`
    parameters used. You can find the result of each verification check performed in the
    appropriate sub-resource: `document`, `id_number`, `selfie`.

    Each VerificationReport contains a copy of any data collected by the user as well as
    reference IDs which can be used to access collected images through the [FileUpload](https://stripe.com/docs/api/files)
    API. To configure and create VerificationReports, use the
    [VerificationSession](https://stripe.com/docs/api/identity/verification_sessions) API.

    Related guide: [Accessing verification results](https://stripe.com/docs/identity/verification-sessions#results).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_reference_id: typing.Optional[str] = pydantic.Field(
        alias="client_reference_id", default=None
    )
    """
    A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    document: typing.Optional[GelatoDocumentReport] = pydantic.Field(
        alias="document", default=None
    )
    """
    Result from a document check
    """
    email: typing.Optional[GelatoEmailReport] = pydantic.Field(
        alias="email", default=None
    )
    """
    Result from a email check
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    id_number: typing.Optional[GelatoIdNumberReport] = pydantic.Field(
        alias="id_number", default=None
    )
    """
    Result from an id_number check
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["identity.verification_report"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    options: typing.Optional[GelatoVerificationReportOptions] = pydantic.Field(
        alias="options", default=None
    )
    phone: typing.Optional[GelatoPhoneReport] = pydantic.Field(
        alias="phone", default=None
    )
    """
    Result from a phone check
    """
    selfie: typing.Optional[GelatoSelfieReport] = pydantic.Field(
        alias="selfie", default=None
    )
    """
    Result from a selfie check
    """
    type_: typing_extensions.Literal["document", "id_number", "verification_flow"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Type of report.
    """
    verification_flow: typing.Optional[str] = pydantic.Field(
        alias="verification_flow", default=None
    )
    """
    The configuration token of a verification flow from the dashboard.
    """
    verification_session: typing.Optional[str] = pydantic.Field(
        alias="verification_session", default=None
    )
    """
    ID of the VerificationSession that created this report.
    """
