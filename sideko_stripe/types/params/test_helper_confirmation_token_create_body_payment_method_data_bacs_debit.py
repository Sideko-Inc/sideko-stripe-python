import pydantic
import typing
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataBacsDebit(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataBacsDebit
    """

    account_number: typing_extensions.NotRequired[str]

    sort_code: typing_extensions.NotRequired[str]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataBacsDebit(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
