import pydantic
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataBoleto(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataBoleto
    """

    tax_id: typing_extensions.Required[str]


class _SerializerSetupIntentCreateBodyPaymentMethodDataBoleto(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: str = pydantic.Field(
        alias="tax_id",
    )
