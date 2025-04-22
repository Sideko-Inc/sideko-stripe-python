import pydantic
import typing_extensions


class CheckoutSessionCreateBodyCustomFieldsItemLabel(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyCustomFieldsItemLabel
    """

    custom: typing_extensions.Required[str]

    type_: typing_extensions.Required[typing_extensions.Literal["custom"]]


class _SerializerCheckoutSessionCreateBodyCustomFieldsItemLabel(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomFieldsItemLabel handling case conversions
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
