import pydantic
import typing
import typing_extensions

from .payment_link_create_body_custom_fields_item_dropdown_options_item import (
    PaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem,
    _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem,
)


class PaymentLinkCreateBodyCustomFieldsItemDropdown(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomFieldsItemDropdown
    """

    default_value: typing_extensions.NotRequired[str]

    options: typing_extensions.Required[
        typing.List[PaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem]
    ]


class _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdown(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomFieldsItemDropdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    options: typing.List[
        _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem
    ] = pydantic.Field(
        alias="options",
    )
