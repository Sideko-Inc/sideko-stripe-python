import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SetupIntentUpdateBodyPaymentMethodDataMetadata
    """


class _SerializerSetupIntentUpdateBodyPaymentMethodDataMetadata(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
