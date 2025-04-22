import pydantic
import typing


class SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference_prefix: typing.Optional[str] = pydantic.Field(
        alias="reference_prefix", default=None
    )
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'STRIPE'.
    """
