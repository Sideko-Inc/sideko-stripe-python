import pydantic
import typing
import typing_extensions

from .gelato_provided_details import GelatoProvidedDetails
from .gelato_session_last_error import GelatoSessionLastError
from .gelato_verification_session_options import GelatoVerificationSessionOptions
from .gelato_verified_outputs import GelatoVerifiedOutputs
from .identity_verification_report import IdentityVerificationReport
from .identity_verification_session_metadata import IdentityVerificationSessionMetadata
from .verification_session_redaction import VerificationSessionRedaction


class IdentityVerificationSession(pydantic.BaseModel):
    """
    A VerificationSession guides you through the process of collecting and verifying the identities
    of your users. It contains details about the type of verification, such as what [verification
    check](/docs/identity/verification-checks) to perform. Only create one VerificationSession for
    each verification in your system.

    A VerificationSession transitions through [multiple
    statuses](/docs/identity/how-sessions-work) throughout its lifetime as it progresses through
    the verification flow. The VerificationSession contains the user's verified data after
    verification checks are complete.

    Related guide: [The Verification Sessions API](https://stripe.com/docs/identity/verification-sessions)
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
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    """
    The short-lived client secret used by Stripe.js to [show a verification modal](https://stripe.com/docs/js/identity/modal) inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on [passing the client secret to the frontend](https://stripe.com/docs/identity/verification-sessions#client-secret) to learn more.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    last_error: typing.Optional[GelatoSessionLastError] = pydantic.Field(
        alias="last_error", default=None
    )
    """
    Shows last VerificationSession error
    """
    last_verification_report: typing.Optional[
        typing.Union[str, IdentityVerificationReport]
    ] = pydantic.Field(alias="last_verification_report", default=None)
    """
    ID of the most recent VerificationReport. [Learn more about accessing detailed verification results.](https://stripe.com/docs/identity/verification-sessions#results)
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: IdentityVerificationSessionMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["identity.verification_session"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    options: typing.Optional[GelatoVerificationSessionOptions] = pydantic.Field(
        alias="options", default=None
    )
    provided_details: typing.Optional[GelatoProvidedDetails] = pydantic.Field(
        alias="provided_details", default=None
    )
    redaction: typing.Optional[VerificationSessionRedaction] = pydantic.Field(
        alias="redaction", default=None
    )
    related_customer: typing.Optional[str] = pydantic.Field(
        alias="related_customer", default=None
    )
    """
    Customer ID
    """
    status: typing_extensions.Literal[
        "canceled", "processing", "requires_input", "verified"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Status of this VerificationSession. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).
    """
    type_: typing_extensions.Literal["document", "id_number", "verification_flow"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on [verifying identity documents](https://stripe.com/docs/identity/verify-identity-documents?platform=web&type=redirect) to learn how to redirect users to Stripe.
    """
    verification_flow: typing.Optional[str] = pydantic.Field(
        alias="verification_flow", default=None
    )
    """
    The configuration token of a verification flow from the dashboard.
    """
    verified_outputs: typing.Optional[GelatoVerifiedOutputs] = pydantic.Field(
        alias="verified_outputs", default=None
    )
