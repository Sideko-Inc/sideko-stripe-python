import pydantic
import typing
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataMetadata
    """


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
