import pydantic


class PaymentLinksResourceCustomFieldsDropdownOption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    label: str = pydantic.Field(
        alias="label",
    )
    """
    The label for the option, displayed to the customer. Up to 100 characters.
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.
    """
