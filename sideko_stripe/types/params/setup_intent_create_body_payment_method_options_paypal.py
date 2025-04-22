import pydantic
import typing
import typing_extensions


class SetupIntentCreateBodyPaymentMethodOptionsPaypal(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodOptionsPaypal
    """

    billing_agreement_id: typing_extensions.NotRequired[str]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsPaypal(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsPaypal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_agreement_id: typing.Optional[str] = pydantic.Field(
        alias="billing_agreement_id", default=None
    )
