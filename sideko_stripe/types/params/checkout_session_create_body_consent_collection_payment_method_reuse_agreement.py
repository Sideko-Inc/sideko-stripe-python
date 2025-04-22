import pydantic
import typing_extensions


class CheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement
    """

    position: typing_extensions.Required[typing_extensions.Literal["auto", "hidden"]]


class _SerializerCheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    position: typing_extensions.Literal["auto", "hidden"] = pydantic.Field(
        alias="position",
    )
