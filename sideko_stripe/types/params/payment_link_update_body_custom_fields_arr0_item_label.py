import pydantic
import typing_extensions


class PaymentLinkUpdateBodyCustomFieldsArr0ItemLabel(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomFieldsArr0ItemLabel
    """

    custom: typing_extensions.Required[str]

    type_: typing_extensions.Required[typing_extensions.Literal["custom"]]


class _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemLabel(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomFieldsArr0ItemLabel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom: str = pydantic.Field(
        alias="custom",
    )
    type_: typing_extensions.Literal["custom"] = pydantic.Field(
        alias="type",
    )
