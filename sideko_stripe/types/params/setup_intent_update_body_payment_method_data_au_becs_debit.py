import pydantic
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataAuBecsDebit(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataAuBecsDebit
    """

    account_number: typing_extensions.Required[str]

    bsb_number: typing_extensions.Required[str]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataAuBecsDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataAuBecsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: str = pydantic.Field(
        alias="account_number",
    )
    bsb_number: str = pydantic.Field(
        alias="bsb_number",
    )
