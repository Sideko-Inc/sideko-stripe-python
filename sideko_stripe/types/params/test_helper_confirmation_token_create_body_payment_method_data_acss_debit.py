import pydantic
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataAcssDebit(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataAcssDebit
    """

    account_number: typing_extensions.Required[str]

    institution_number: typing_extensions.Required[str]

    transit_number: typing_extensions.Required[str]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataAcssDebit(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataAcssDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: str = pydantic.Field(
        alias="account_number",
    )
    institution_number: str = pydantic.Field(
        alias="institution_number",
    )
    transit_number: str = pydantic.Field(
        alias="transit_number",
    )
