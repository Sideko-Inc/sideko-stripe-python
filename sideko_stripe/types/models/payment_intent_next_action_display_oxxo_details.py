import pydantic
import typing


class PaymentIntentNextActionDisplayOxxoDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_after: typing.Optional[int] = pydantic.Field(
        alias="expires_after", default=None
    )
    """
    The timestamp after which the OXXO voucher expires.
    """
    hosted_voucher_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_voucher_url", default=None
    )
    """
    The URL for the hosted OXXO voucher page, which allows customers to view and print an OXXO voucher.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    OXXO reference number.
    """
