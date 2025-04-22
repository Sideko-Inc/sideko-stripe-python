import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodOptionsPaypal(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsPaypal
    """

    billing_agreement_id: typing_extensions.NotRequired[str]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsPaypal(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsPaypal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_agreement_id: typing.Optional[str] = pydantic.Field(
        alias="billing_agreement_id", default=None
    )
