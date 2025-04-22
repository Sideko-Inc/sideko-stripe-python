import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsSwish(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsSwish
    """

    reference: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsSwish(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsSwish handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
