import pydantic
import typing_extensions


class CustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item(
    typing_extensions.TypedDict
):
    """
    CustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item
    """

    name: typing_extensions.Required[str]

    value: typing_extensions.Required[str]


class _SerializerCustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for CustomerCreateBodyInvoiceSettingsCustomFieldsArr0Item handling case conversions
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
