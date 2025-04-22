import pydantic
import typing
import typing_extensions

from .issuing_network_token_address import IssuingNetworkTokenAddress


class IssuingNetworkTokenWalletProvider(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="account_id", default=None)
    """
    The wallet provider-given account ID of the digital wallet the token belongs to.
    """
    account_trust_score: typing.Optional[int] = pydantic.Field(
        alias="account_trust_score", default=None
    )
    """
    An evaluation on the trustworthiness of the wallet account between 1 and 5. A higher score indicates more trustworthy.
    """
    card_number_source: typing.Optional[
        typing_extensions.Literal["app", "manual", "on_file", "other"]
    ] = pydantic.Field(alias="card_number_source", default=None)
    """
    The method used for tokenizing a card.
    """
    cardholder_address: typing.Optional[IssuingNetworkTokenAddress] = pydantic.Field(
        alias="cardholder_address", default=None
    )
    cardholder_name: typing.Optional[str] = pydantic.Field(
        alias="cardholder_name", default=None
    )
    """
    The name of the cardholder tokenizing the card.
    """
    device_trust_score: typing.Optional[int] = pydantic.Field(
        alias="device_trust_score", default=None
    )
    """
    An evaluation on the trustworthiness of the device. A higher score indicates more trustworthy.
    """
    hashed_account_email_address: typing.Optional[str] = pydantic.Field(
        alias="hashed_account_email_address", default=None
    )
    """
    The hashed email address of the cardholder's account with the wallet provider.
    """
    reason_codes: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "account_card_too_new",
                "account_recently_changed",
                "account_too_new",
                "account_too_new_since_launch",
                "additional_device",
                "data_expired",
                "defer_id_v_decision",
                "device_recently_lost",
                "good_activity_history",
                "has_suspended_tokens",
                "high_risk",
                "inactive_account",
                "long_account_tenure",
                "low_account_score",
                "low_device_score",
                "low_phone_number_score",
                "network_service_error",
                "outside_home_territory",
                "provisioning_cardholder_mismatch",
                "provisioning_device_and_cardholder_mismatch",
                "provisioning_device_mismatch",
                "same_device_no_prior_authentication",
                "same_device_successful_prior_authentication",
                "software_update",
                "suspicious_activity",
                "too_many_different_cardholders",
                "too_many_recent_attempts",
                "too_many_recent_tokens",
            ]
        ]
    ] = pydantic.Field(alias="reason_codes", default=None)
    """
    The reasons for suggested tokenization given by the card network.
    """
    suggested_decision: typing.Optional[
        typing_extensions.Literal["approve", "decline", "require_auth"]
    ] = pydantic.Field(alias="suggested_decision", default=None)
    """
    The recommendation on responding to the tokenization request.
    """
    suggested_decision_version: typing.Optional[str] = pydantic.Field(
        alias="suggested_decision_version", default=None
    )
    """
    The version of the standard for mapping reason codes followed by the wallet provider.
    """
