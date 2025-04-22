import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .charge import Charge
    from .payment_intent import PaymentIntent


class RadarEarlyFraudWarning(pydantic.BaseModel):
    """
    An early fraud warning indicates that the card issuer has notified us that a
    charge may be fraudulent.

    Related guide: [Early fraud warnings](https://stripe.com/docs/disputes/measuring#early-fraud-warnings)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actionable: bool = pydantic.Field(
        alias="actionable",
    )
    """
    An EFW is actionable if it has not received a dispute and has not been fully refunded. You may wish to proactively refund a charge that receives an EFW, in order to avoid receiving a dispute later.
    """
    charge: typing.Union[str, "Charge"] = pydantic.Field(
        alias="charge",
    )
    """
    ID of the charge this early fraud warning is for, optionally expanded.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    fraud_type: str = pydantic.Field(
        alias="fraud_type",
    )
    """
    The type of fraud labelled by the issuer. One of `card_never_received`, `fraudulent_card_application`, `made_with_counterfeit_card`, `made_with_lost_card`, `made_with_stolen_card`, `misc`, `unauthorized_use_of_card`.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["radar.early_fraud_warning"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    ID of the Payment Intent this early fraud warning is for, optionally expanded.
    """
