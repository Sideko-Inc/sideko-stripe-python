import pydantic
import typing
import typing_extensions


class ThreeDSecureDetailsCharge(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authentication_flow: typing.Optional[
        typing_extensions.Literal["challenge", "frictionless"]
    ] = pydantic.Field(alias="authentication_flow", default=None)
    """
    For authenticated transactions: how the customer was authenticated by
    the issuing bank.
    """
    electronic_commerce_indicator: typing.Optional[
        typing_extensions.Literal["01", "02", "05", "06", "07"]
    ] = pydantic.Field(alias="electronic_commerce_indicator", default=None)
    """
    The Electronic Commerce Indicator (ECI). A protocol-level field
    indicating what degree of authentication was performed.
    """
    exemption_indicator: typing.Optional[
        typing_extensions.Literal["low_risk", "none"]
    ] = pydantic.Field(alias="exemption_indicator", default=None)
    """
    The exemption requested via 3DS and accepted by the issuer at authentication time.
    """
    exemption_indicator_applied: typing.Optional[bool] = pydantic.Field(
        alias="exemption_indicator_applied", default=None
    )
    """
    Whether Stripe requested the value of `exemption_indicator` in the transaction. This will depend on
    the outcome of Stripe's internal risk assessment.
    """
    result: typing.Optional[
        typing_extensions.Literal[
            "attempt_acknowledged",
            "authenticated",
            "exempted",
            "failed",
            "not_supported",
            "processing_error",
        ]
    ] = pydantic.Field(alias="result", default=None)
    """
    Indicates the outcome of 3D Secure authentication.
    """
    result_reason: typing.Optional[
        typing_extensions.Literal[
            "abandoned",
            "bypassed",
            "canceled",
            "card_not_enrolled",
            "network_not_supported",
            "protocol_error",
            "rejected",
        ]
    ] = pydantic.Field(alias="result_reason", default=None)
    """
    Additional information about why 3D Secure succeeded or failed based
    on the `result`.
    """
    transaction_id: typing.Optional[str] = pydantic.Field(
        alias="transaction_id", default=None
    )
    """
    The 3D Secure 1 XID or 3D Secure 2 Directory Server Transaction ID
    (dsTransId) for this payment.
    """
    version: typing.Optional[typing_extensions.Literal["1.0.2", "2.1.0", "2.2.0"]] = (
        pydantic.Field(alias="version", default=None)
    )
    """
    The version of 3D Secure that was used.
    """
