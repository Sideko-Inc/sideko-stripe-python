import pydantic
import typing_extensions


class PaymentLinkCreateBodyCustomFieldsItemLabel(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyCustomFieldsItemLabel
    """

    custom: typing_extensions.Required[str]

    type_: typing_extensions.Required[typing_extensions.Literal["custom"]]


class _SerializerPaymentLinkCreateBodyCustomFieldsItemLabel(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomFieldsItemLabel handling case conversions
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
