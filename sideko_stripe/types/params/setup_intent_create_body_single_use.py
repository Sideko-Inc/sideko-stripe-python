import pydantic
import typing_extensions


class SetupIntentCreateBodySingleUse(typing_extensions.TypedDict):
    """
    If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.

    Single-use mandates are only valid for the following payment methods: `acss_debit`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `ideal`, `link`, `sepa_debit`, and `us_bank_account`.
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]


class _SerializerSetupIntentCreateBodySingleUse(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodySingleUse handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
