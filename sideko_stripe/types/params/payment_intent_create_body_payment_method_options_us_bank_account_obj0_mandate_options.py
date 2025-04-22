import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions
    """

    collection_method: typing_extensions.NotRequired[typing_extensions.Literal["paper"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    collection_method: typing.Optional[typing_extensions.Literal["paper"]] = (
        pydantic.Field(alias="collection_method", default=None)
    )
