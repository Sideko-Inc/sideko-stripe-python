import pydantic
import typing_extensions


class PaymentMethodCreateBodySofort(typing_extensions.TypedDict):
    """
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerPaymentMethodCreateBodySofort(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodySofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"] = (
        pydantic.Field(
            alias="country",
        )
    )
