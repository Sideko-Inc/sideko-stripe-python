import pydantic
import typing_extensions


class InvoicePaymentMethodOptionsBancontact(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    preferred_language: typing_extensions.Literal["de", "en", "fr", "nl"] = (
        pydantic.Field(
            alias="preferred_language",
        )
    )
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """
