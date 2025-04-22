import pydantic
import typing


class PaymentMethodDetailsLink(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the funding source country beneath the Link payment.
    You could use this attribute to get a sense of international fees.
    """
