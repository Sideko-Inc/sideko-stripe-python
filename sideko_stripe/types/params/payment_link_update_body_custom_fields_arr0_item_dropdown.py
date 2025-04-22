import pydantic
import typing
import typing_extensions

from .payment_link_update_body_custom_fields_arr0_item_dropdown_options_item import (
    PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem,
)


class PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown
    """

    default_value: typing_extensions.NotRequired[str]

    options: typing_extensions.Required[
        typing.List[PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem]
    ]


class _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    options: typing.List[
        _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem
    ] = pydantic.Field(
        alias="options",
    )
