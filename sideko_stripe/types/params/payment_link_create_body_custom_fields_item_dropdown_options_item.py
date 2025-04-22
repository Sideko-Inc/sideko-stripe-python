import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem(
    typing_extensions.TypedDict
):
    """
    PaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem
    """

    label: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodyCustomFieldsItemDropdownOptionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    label: str = pydantic.Field(
        alias="label",
    )
    value: str = pydantic.Field(
        alias="value",
    )
