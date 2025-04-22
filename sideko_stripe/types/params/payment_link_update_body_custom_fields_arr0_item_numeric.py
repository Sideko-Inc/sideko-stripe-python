import pydantic
import typing
import typing_extensions


class PaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric
    """

    default_value: typing_extensions.NotRequired[str]

    maximum_length: typing_extensions.NotRequired[int]

    minimum_length: typing_extensions.NotRequired[int]


class _SerializerPaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomFieldsArr0ItemNumeric handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    maximum_length: typing.Optional[int] = pydantic.Field(
        alias="maximum_length", default=None
    )
    minimum_length: typing.Optional[int] = pydantic.Field(
        alias="minimum_length", default=None
    )
