import pydantic
import typing
import typing_extensions


class PaymentPagesCheckoutSessionConsent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    promotions: typing.Optional[typing_extensions.Literal["opt_in", "opt_out"]] = (
        pydantic.Field(alias="promotions", default=None)
    )
    """
    If `opt_in`, the customer consents to receiving promotional communications
    from the merchant about this Checkout Session.
    """
    terms_of_service: typing.Optional[typing_extensions.Literal["accepted"]] = (
        pydantic.Field(alias="terms_of_service", default=None)
    )
    """
    If `accepted`, the customer in this Checkout Session has agreed to the merchant's terms of service.
    """
