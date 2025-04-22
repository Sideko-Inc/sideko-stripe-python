import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem
    """

    label: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodyCustomFieldsArr0ItemDropdownOptionsItem handling case conversions
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
