import pydantic
import typing


class PaymentIntentNextActionBoleto(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The timestamp after which the boleto expires.
    """
    hosted_voucher_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_voucher_url", default=None
    )
    """
    The URL to the hosted boleto voucher page, which allows customers to view the boleto voucher.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    The boleto number.
    """
    pdf: typing.Optional[str] = pydantic.Field(alias="pdf", default=None)
    """
    The URL to the downloadable boleto voucher PDF.
    """
