import pydantic
import typing
import typing_extensions


class IssuingAuthorizationFraudChallenge(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    channel: typing_extensions.Literal["sms"] = pydantic.Field(
        alias="channel",
    )
    """
    The method by which the fraud challenge was delivered to the cardholder.
    """
    status: typing_extensions.Literal[
        "expired", "pending", "rejected", "undeliverable", "verified"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the fraud challenge.
    """
    undeliverable_reason: typing.Optional[
        typing_extensions.Literal["no_phone_number", "unsupported_phone_number"]
    ] = pydantic.Field(alias="undeliverable_reason", default=None)
    """
    If the challenge is not deliverable, the reason why.
    """
