import pydantic
import typing
import typing_extensions

from .payment_link_create_body_custom_fields_item_dropdown import (
    PaymentLinkCreateBodyCustomFieldsItemDropdown,
    _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdown,
)
from .payment_link_create_body_custom_fields_item_label import (
    PaymentLinkCreateBodyCustomFieldsItemLabel,
    _SerializerPaymentLinkCreateBodyCustomFieldsItemLabel,
)
from .payment_link_create_body_custom_fields_item_numeric import (
    PaymentLinkCreateBodyCustomFieldsItemNumeric,
    _SerializerPaymentLinkCreateBodyCustomFieldsItemNumeric,
)
from .payment_link_create_body_custom_fields_item_text import (
    PaymentLinkCreateBodyCustomFieldsItemText,
    _SerializerPaymentLinkCreateBodyCustomFieldsItemText,
)


class PaymentLinkCreateBodyCustomFieldsItem(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomFieldsItem
    """

    dropdown: typing_extensions.NotRequired[
        PaymentLinkCreateBodyCustomFieldsItemDropdown
    ]

    key: typing_extensions.Required[str]

    label: typing_extensions.Required[PaymentLinkCreateBodyCustomFieldsItemLabel]

    numeric: typing_extensions.NotRequired[PaymentLinkCreateBodyCustomFieldsItemNumeric]

    optional: typing_extensions.NotRequired[bool]

    text: typing_extensions.NotRequired[PaymentLinkCreateBodyCustomFieldsItemText]

    type_: typing_extensions.Required[
        typing_extensions.Literal["dropdown", "numeric", "text"]
    ]


class _SerializerPaymentLinkCreateBodyCustomFieldsItem(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomFieldsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dropdown: typing.Optional[
        _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdown
    ] = pydantic.Field(alias="dropdown", default=None)
    key: str = pydantic.Field(
        alias="key",
    )
    label: _SerializerPaymentLinkCreateBodyCustomFieldsItemLabel = pydantic.Field(
        alias="label",
    )
    numeric: typing.Optional[
        _SerializerPaymentLinkCreateBodyCustomFieldsItemNumeric
    ] = pydantic.Field(alias="numeric", default=None)
    optional: typing.Optional[bool] = pydantic.Field(alias="optional", default=None)
    text: typing.Optional[_SerializerPaymentLinkCreateBodyCustomFieldsItemText] = (
        pydantic.Field(alias="text", default=None)
    )
    type_: typing_extensions.Literal["dropdown", "numeric", "text"] = pydantic.Field(
        alias="type",
    )
