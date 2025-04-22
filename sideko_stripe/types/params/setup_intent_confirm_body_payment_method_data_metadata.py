import pydantic
import typing
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SetupIntentConfirmBodyPaymentMethodDataMetadata
    """


class _SerializerSetupIntentConfirmBodyPaymentMethodDataMetadata(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
