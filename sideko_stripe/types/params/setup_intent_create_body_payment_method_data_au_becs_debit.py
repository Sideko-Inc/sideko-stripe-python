import pydantic
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataAuBecsDebit(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataAuBecsDebit
    """

    account_number: typing_extensions.Required[str]

    bsb_number: typing_extensions.Required[str]


class _SerializerSetupIntentCreateBodyPaymentMethodDataAuBecsDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataAuBecsDebit handling case conversions
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
