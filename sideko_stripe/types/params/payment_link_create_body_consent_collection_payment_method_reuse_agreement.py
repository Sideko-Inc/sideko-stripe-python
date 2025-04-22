import pydantic
import typing_extensions


class PaymentLinkCreateBodyConsentCollectionPaymentMethodReuseAgreement(
    typing_extensions.TypedDict
):
    """
    PaymentLinkCreateBodyConsentCollectionPaymentMethodReuseAgreement
    """

    position: typing_extensions.Required[typing_extensions.Literal["auto", "hidden"]]


class _SerializerPaymentLinkCreateBodyConsentCollectionPaymentMethodReuseAgreement(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodyConsentCollectionPaymentMethodReuseAgreement handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    position: typing_extensions.Literal["auto", "hidden"] = pydantic.Field(
        alias="position",
    )
