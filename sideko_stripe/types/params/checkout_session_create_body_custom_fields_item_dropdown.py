import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_custom_fields_item_dropdown_options_item import (
    CheckoutSessionCreateBodyCustomFieldsItemDropdownOptionsItem,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItemDropdownOptionsItem,
)


class CheckoutSessionCreateBodyCustomFieldsItemDropdown(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyCustomFieldsItemDropdown
    """

    default_value: typing_extensions.NotRequired[str]

    options: typing_extensions.Required[
        typing.List[CheckoutSessionCreateBodyCustomFieldsItemDropdownOptionsItem]
    ]


class _SerializerCheckoutSessionCreateBodyCustomFieldsItemDropdown(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomFieldsItemDropdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    options: typing.List[
        _SerializerCheckoutSessionCreateBodyCustomFieldsItemDropdownOptionsItem
    ] = pydantic.Field(
        alias="options",
    )
