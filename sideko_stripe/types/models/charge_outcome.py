import pydantic
import typing
import typing_extensions

from .rule import Rule


class ChargeOutcome(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    advice_code: typing.Optional[
        typing_extensions.Literal[
            "confirm_card_data", "do_not_try_again", "try_again_later"
        ]
    ] = pydantic.Field(alias="advice_code", default=None)
    """
    An enumerated value providing a more detailed explanation on [how to proceed with an error](https://stripe.com/docs/declines#retrying-issuer-declines).
    """
    network_advice_code: typing.Optional[str] = pydantic.Field(
        alias="network_advice_code", default=None
    )
    """
    For charges declined by the network, a 2 digit code which indicates the advice returned by the network on how to proceed with an error.
    """
    network_decline_code: typing.Optional[str] = pydantic.Field(
        alias="network_decline_code", default=None
    )
    """
    For charges declined by the network, a brand specific 2, 3, or 4 digit code which indicates the reason the authorization failed.
    """
    network_status: typing.Optional[str] = pydantic.Field(
        alias="network_status", default=None
    )
    """
    Possible values are `approved_by_network`, `declined_by_network`, `not_sent_to_network`, and `reversed_after_approval`. The value `reversed_after_approval` indicates the payment was [blocked by Stripe](https://stripe.com/docs/declines#blocked-payments) after bank authorization, and may temporarily appear as "pending" on a cardholder's statement.
    """
    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
    """
    An enumerated value providing a more detailed explanation of the outcome's `type`. Charges blocked by Radar's default block rule have the value `highest_risk_level`. Charges placed in review by Radar's default review rule have the value `elevated_risk_level`. Charges authorized, blocked, or placed in review by custom rules have the value `rule`. See [understanding declines](https://stripe.com/docs/declines) for more details.
    """
    risk_level: typing.Optional[str] = pydantic.Field(alias="risk_level", default=None)
    """
    Stripe Radar's evaluation of the riskiness of the payment. Possible values for evaluated payments are `normal`, `elevated`, `highest`. For non-card payments, and card-based payments predating the public assignment of risk levels, this field will have the value `not_assessed`. In the event of an error in the evaluation, this field will have the value `unknown`. This field is only available with Radar.
    """
    risk_score: typing.Optional[int] = pydantic.Field(alias="risk_score", default=None)
    """
    Stripe Radar's evaluation of the riskiness of the payment. Possible values for evaluated payments are between 0 and 100. For non-card payments, card-based payments predating the public assignment of risk scores, or in the event of an error during evaluation, this field will not be present. This field is only available with Radar for Fraud Teams.
    """
    rule: typing.Optional[typing.Union[str, Rule]] = pydantic.Field(
        alias="rule", default=None
    )
    """
    The ID of the Radar rule that matched the payment, if applicable.
    """
    seller_message: typing.Optional[str] = pydantic.Field(
        alias="seller_message", default=None
    )
    """
    A human-readable description of the outcome type and reason, designed for you (the recipient of the payment), not your customer.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    Possible values are `authorized`, `manual_review`, `issuer_declined`, `blocked`, and `invalid`. See [understanding declines](https://stripe.com/docs/declines) and [Radar reviews](https://stripe.com/docs/radar/reviews) for details.
    """
