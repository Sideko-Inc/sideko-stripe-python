import pydantic
import typing_extensions


class CustomerUpdateBodyInvoiceSettingsCustomFieldsArr0Item(
    typing_extensions.TypedDict
):
    """
    CustomerUpdateBodyInvoiceSettingsCustomFieldsArr0Item
    """

    name: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerCustomerUpdateBodyInvoiceSettingsCustomFieldsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for CustomerUpdateBodyInvoiceSettingsCustomFieldsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
    value: str = pydantic.Field(
        alias="value",
    )
