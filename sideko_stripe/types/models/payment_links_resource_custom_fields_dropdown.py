import pydantic
import typing

from .payment_links_resource_custom_fields_dropdown_option import (
    PaymentLinksResourceCustomFieldsDropdownOption,
)


class PaymentLinksResourceCustomFieldsDropdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    """
    The value that will pre-fill on the payment page.
    """
    options: typing.List[PaymentLinksResourceCustomFieldsDropdownOption] = (
        pydantic.Field(
            alias="options",
        )
    )
    """
    The options available for the customer to select. Up to 200 options allowed.
    """
