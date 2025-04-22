import pydantic
import typing


class PaymentIntentNextActionDisplayMultibancoDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    entity: typing.Optional[str] = pydantic.Field(alias="entity", default=None)
    """
    Entity number associated with this Multibanco payment.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The timestamp at which the Multibanco voucher expires.
    """
    hosted_voucher_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_voucher_url", default=None
    )
    """
    The URL for the hosted Multibanco voucher page, which allows customers to view a Multibanco voucher.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Reference number associated with this Multibanco payment.
    """
