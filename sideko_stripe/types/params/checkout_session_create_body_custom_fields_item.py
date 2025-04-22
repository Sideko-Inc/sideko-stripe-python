import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_custom_fields_item_dropdown import (
    CheckoutSessionCreateBodyCustomFieldsItemDropdown,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItemDropdown,
)
from .checkout_session_create_body_custom_fields_item_label import (
    CheckoutSessionCreateBodyCustomFieldsItemLabel,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItemLabel,
)
from .checkout_session_create_body_custom_fields_item_numeric import (
    CheckoutSessionCreateBodyCustomFieldsItemNumeric,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItemNumeric,
)
from .checkout_session_create_body_custom_fields_item_text import (
    CheckoutSessionCreateBodyCustomFieldsItemText,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItemText,
)


class CheckoutSessionCreateBodyCustomFieldsItem(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyCustomFieldsItem
    """

    dropdown: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyCustomFieldsItemDropdown
    ]

    key: typing_extensions.Required[str]

    label: typing_extensions.Required[CheckoutSessionCreateBodyCustomFieldsItemLabel]

    numeric: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyCustomFieldsItemNumeric
    ]

    optional: typing_extensions.NotRequired[bool]

    text: typing_extensions.NotRequired[CheckoutSessionCreateBodyCustomFieldsItemText]

    type_: typing_extensions.Required[
        typing_extensions.Literal["dropdown", "numeric", "text"]
    ]


class _SerializerCheckoutSessionCreateBodyCustomFieldsItem(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomFieldsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dropdown: typing.Optional[
        _SerializerCheckoutSessionCreateBodyCustomFieldsItemDropdown
    ] = pydantic.Field(alias="dropdown", default=None)
    key: str = pydantic.Field(
        alias="key",
    )
    label: _SerializerCheckoutSessionCreateBodyCustomFieldsItemLabel = pydantic.Field(
        alias="label",
    )
    numeric: typing.Optional[
        _SerializerCheckoutSessionCreateBodyCustomFieldsItemNumeric
    ] = pydantic.Field(alias="numeric", default=None)
    optional: typing.Optional[bool] = pydantic.Field(alias="optional", default=None)
    text: typing.Optional[_SerializerCheckoutSessionCreateBodyCustomFieldsItemText] = (
        pydantic.Field(alias="text", default=None)
    )
    type_: typing_extensions.Literal["dropdown", "numeric", "text"] = pydantic.Field(
        alias="type",
    )
