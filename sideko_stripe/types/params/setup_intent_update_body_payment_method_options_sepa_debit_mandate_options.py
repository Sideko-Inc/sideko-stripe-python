import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions
    """

    reference_prefix: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reference_prefix: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="reference_prefix", default=None
    )
