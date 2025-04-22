import pydantic
import typing
import typing_extensions


class PaymentLinkUpdateBodyTaxIdCollection(typing_extensions.TypedDict):
    """
    Controls tax ID collection during checkout.
    """

    enabled: typing_extensions.Required[bool]

    required: typing_extensions.NotRequired[
        typing_extensions.Literal["if_supported", "never"]
    ]


class _SerializerPaymentLinkUpdateBodyTaxIdCollection(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyTaxIdCollection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    required: typing.Optional[typing_extensions.Literal["if_supported", "never"]] = (
        pydantic.Field(alias="required", default=None)
    )
