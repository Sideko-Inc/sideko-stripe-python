import pydantic
import typing
import typing_extensions

from .payment_pages_checkout_session_custom_fields_dropdown import (
    PaymentPagesCheckoutSessionCustomFieldsDropdown,
)
from .payment_pages_checkout_session_custom_fields_label import (
    PaymentPagesCheckoutSessionCustomFieldsLabel,
)
from .payment_pages_checkout_session_custom_fields_numeric import (
    PaymentPagesCheckoutSessionCustomFieldsNumeric,
)
from .payment_pages_checkout_session_custom_fields_text import (
    PaymentPagesCheckoutSessionCustomFieldsText,
)


class PaymentPagesCheckoutSessionCustomFields(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dropdown: typing.Optional[PaymentPagesCheckoutSessionCustomFieldsDropdown] = (
        pydantic.Field(alias="dropdown", default=None)
    )
    key: str = pydantic.Field(
        alias="key",
    )
    """
    String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.
    """
    label: PaymentPagesCheckoutSessionCustomFieldsLabel = pydantic.Field(
        alias="label",
    )
    numeric: typing.Optional[PaymentPagesCheckoutSessionCustomFieldsNumeric] = (
        pydantic.Field(alias="numeric", default=None)
    )
    optional: bool = pydantic.Field(
        alias="optional",
    )
    """
    Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.
    """
    text: typing.Optional[PaymentPagesCheckoutSessionCustomFieldsText] = pydantic.Field(
        alias="text", default=None
    )
    type_: typing_extensions.Literal["dropdown", "numeric", "text"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the field.
    """
