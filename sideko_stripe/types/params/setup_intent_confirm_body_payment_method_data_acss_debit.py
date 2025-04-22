import pydantic
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataAcssDebit(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataAcssDebit
    """

    account_number: typing_extensions.Required[str]

    institution_number: typing_extensions.Required[str]

    transit_number: typing_extensions.Required[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataAcssDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataAcssDebit handling case conversions
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
