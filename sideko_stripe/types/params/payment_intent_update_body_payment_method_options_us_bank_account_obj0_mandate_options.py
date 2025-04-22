import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions
    """

    collection_method: typing_extensions.NotRequired[typing_extensions.Literal["paper"]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    collection_method: typing.Optional[typing_extensions.Literal["paper"]] = (
        pydantic.Field(alias="collection_method", default=None)
    )
