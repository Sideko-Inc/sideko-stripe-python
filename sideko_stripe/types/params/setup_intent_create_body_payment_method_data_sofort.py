import pydantic
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataSofort(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataSofort
    """

    country: typing_extensions.Required[
        typing_extensions.Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodDataSofort(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataSofort handling case conversions
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
