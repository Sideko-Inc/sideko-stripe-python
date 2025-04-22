import pydantic


class InvoiceSettingCustomField(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name of the custom field.
    """
    value: str = pydantic.Field(
        alias="value",
    )
    """
    The value of the custom field.
    """
