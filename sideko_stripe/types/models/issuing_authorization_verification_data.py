import pydantic
import typing
import typing_extensions

from .issuing_authorization_authentication_exemption import (
    IssuingAuthorizationAuthenticationExemption,
)
from .issuing_authorization_three_d_secure import IssuingAuthorizationThreeDSecure


class IssuingAuthorizationVerificationData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_line1_check: typing_extensions.Literal[
        "match", "mismatch", "not_provided"
    ] = pydantic.Field(
        alias="address_line1_check",
    )
    """
    Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`.
    """
    address_postal_code_check: typing_extensions.Literal[
        "match", "mismatch", "not_provided"
    ] = pydantic.Field(
        alias="address_postal_code_check",
    )
    """
    Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`.
    """
    authentication_exemption: typing.Optional[
        IssuingAuthorizationAuthenticationExemption
    ] = pydantic.Field(alias="authentication_exemption", default=None)
    cvc_check: typing_extensions.Literal["match", "mismatch", "not_provided"] = (
        pydantic.Field(
            alias="cvc_check",
        )
    )
    """
    Whether the cardholder provided a CVC and if it matched Stripe’s record.
    """
    expiry_check: typing_extensions.Literal["match", "mismatch", "not_provided"] = (
        pydantic.Field(
            alias="expiry_check",
        )
    )
    """
    Whether the cardholder provided an expiry date and if it matched Stripe’s record.
    """
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    """
    The postal code submitted as part of the authorization used for postal code verification.
    """
    three_d_secure: typing.Optional[IssuingAuthorizationThreeDSecure] = pydantic.Field(
        alias="three_d_secure", default=None
    )
