import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentIntentDataTransferData(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentIntentDataTransferData
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerCheckoutSessionCreateBodyPaymentIntentDataTransferData(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentIntentDataTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
