import pydantic
import typing

from .klarna_payer_details import KlarnaPayerDetails


class PaymentMethodDetailsKlarna(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payer_details: typing.Optional[KlarnaPayerDetails] = pydantic.Field(
        alias="payer_details", default=None
    )
    payment_method_category: typing.Optional[str] = pydantic.Field(
        alias="payment_method_category", default=None
    )
    """
    The Klarna payment method used for this transaction.
    Can be one of `pay_later`, `pay_now`, `pay_with_financing`, or `pay_in_installments`
    """
    preferred_locale: typing.Optional[str] = pydantic.Field(
        alias="preferred_locale", default=None
    )
    """
    Preferred language of the Klarna authorization page that the customer is redirected to.
    Can be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`, `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`, `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`, `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `cs-CZ`, `en-CZ`, `ro-RO`, `en-RO`, `el-GR`, `en-GR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`, `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`
    """
