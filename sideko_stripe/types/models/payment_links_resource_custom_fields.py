import pydantic
import typing
import typing_extensions

from .payment_links_resource_custom_fields_dropdown import (
    PaymentLinksResourceCustomFieldsDropdown,
)
from .payment_links_resource_custom_fields_label import (
    PaymentLinksResourceCustomFieldsLabel,
)
from .payment_links_resource_custom_fields_numeric import (
    PaymentLinksResourceCustomFieldsNumeric,
)
from .payment_links_resource_custom_fields_text import (
    PaymentLinksResourceCustomFieldsText,
)


class PaymentLinksResourceCustomFields(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dropdown: typing.Optional[PaymentLinksResourceCustomFieldsDropdown] = (
        pydantic.Field(alias="dropdown", default=None)
    )
    key: str = pydantic.Field(
        alias="key",
    )
    """
    String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.
    """
    label: PaymentLinksResourceCustomFieldsLabel = pydantic.Field(
        alias="label",
    )
    numeric: typing.Optional[PaymentLinksResourceCustomFieldsNumeric] = pydantic.Field(
        alias="numeric", default=None
    )
    optional: bool = pydantic.Field(
        alias="optional",
    )
    """
    Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.
    """
    text: typing.Optional[PaymentLinksResourceCustomFieldsText] = pydantic.Field(
        alias="text", default=None
    )
    type_: typing_extensions.Literal["dropdown", "numeric", "text"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the field.
    """
