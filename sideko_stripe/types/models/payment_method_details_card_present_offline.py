import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsCardPresentOffline(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    stored_at: typing.Optional[int] = pydantic.Field(alias="stored_at", default=None)
    """
    Time at which the payment was collected while offline
    """
    type_: typing.Optional[typing_extensions.Literal["deferred"]] = pydantic.Field(
        alias="type", default=None
    )
    """
    The method used to process this payment method offline. Only deferred is allowed.
    """
