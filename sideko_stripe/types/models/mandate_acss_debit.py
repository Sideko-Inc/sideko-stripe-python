import pydantic
import typing
import typing_extensions


class MandateAcssDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_for: typing.Optional[
        typing.List[typing_extensions.Literal["invoice", "subscription"]]
    ] = pydantic.Field(alias="default_for", default=None)
    """
    List of Stripe products where this mandate can be selected automatically.
    """
    interval_description: typing.Optional[str] = pydantic.Field(
        alias="interval_description", default=None
    )
    """
    Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'.
    """
    payment_schedule: typing_extensions.Literal["combined", "interval", "sporadic"] = (
        pydantic.Field(
            alias="payment_schedule",
        )
    )
    """
    Payment schedule for the mandate.
    """
    transaction_type: typing_extensions.Literal["business", "personal"] = (
        pydantic.Field(
            alias="transaction_type",
        )
    )
    """
    Transaction type of the mandate.
    """
