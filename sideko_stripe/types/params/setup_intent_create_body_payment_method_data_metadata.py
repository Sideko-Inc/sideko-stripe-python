import pydantic
import typing
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SetupIntentCreateBodyPaymentMethodDataMetadata
    """


class _SerializerSetupIntentCreateBodyPaymentMethodDataMetadata(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
