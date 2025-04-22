import pydantic
import typing
import typing_extensions


class PaymentLinksResourceCustomFieldsLabel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    custom: typing.Optional[str] = pydantic.Field(alias="custom", default=None)
    """
    Custom text for the label, displayed to the customer. Up to 50 characters.
    """
    type_: typing_extensions.Literal["custom"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the label.
    """
