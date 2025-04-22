import pydantic
import typing
import typing_extensions

from .payment_link_update_body_custom_fields_arr0_item_dropdown import (
    PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown,
)
from .payment_link_update_body_custom_fields_arr0_item_label import (
    PaymentLinkUpdateBodyCustomFieldsArr0ItemLabel,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemLabel,
)
from .payment_link_update_body_custom_fields_arr0_item_numeric import (
    PaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric,
)
from .payment_link_update_body_custom_fields_arr0_item_text import (
    PaymentLinkUpdateBodyCustomFieldsArr0ItemText,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemText,
)


class PaymentLinkUpdateBodyCustomFieldsArr0Item(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomFieldsArr0Item
    """

    dropdown: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown
    ]

    key: typing_extensions.Required[str]

    label: typing_extensions.Required[PaymentLinkUpdateBodyCustomFieldsArr0ItemLabel]

    numeric: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric
    ]

    optional: typing_extensions.NotRequired[bool]

    text: typing_extensions.NotRequired[PaymentLinkUpdateBodyCustomFieldsArr0ItemText]

    type_: typing_extensions.Required[
        typing_extensions.Literal["dropdown", "numeric", "text"]
    ]


class _SerializerPaymentLinkUpdateBodyCustomFieldsArr0Item(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomFieldsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dropdown: typing.Optional[
        _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown
    ] = pydantic.Field(alias="dropdown", default=None)
    key: str = pydantic.Field(
        alias="key",
    )
    label: _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemLabel = pydantic.Field(
        alias="label",
    )
    numeric: typing.Optional[
        _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric
    ] = pydantic.Field(alias="numeric", default=None)
    optional: typing.Optional[bool] = pydantic.Field(alias="optional", default=None)
    text: typing.Optional[_SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemText] = (
        pydantic.Field(alias="text", default=None)
    )
    type_: typing_extensions.Literal["dropdown", "numeric", "text"] = pydantic.Field(
        alias="type",
    )
