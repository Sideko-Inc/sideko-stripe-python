import pydantic
import typing


class PaymentLinksResourceCustomFieldsText(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    """
    The value that will pre-fill the field on the payment page.
    """
    maximum_length: typing.Optional[int] = pydantic.Field(
        alias="maximum_length", default=None
    )
    """
    The maximum character length constraint for the customer's input.
    """
    minimum_length: typing.Optional[int] = pydantic.Field(
        alias="minimum_length", default=None
    )
    """
    The minimum character length requirement for the customer's input.
    """
