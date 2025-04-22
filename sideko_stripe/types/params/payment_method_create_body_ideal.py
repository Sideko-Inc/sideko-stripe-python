import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyIdeal(typing_extensions.TypedDict):
    """
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    """

    bank: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "abn_amro",
            "asn_bank",
            "bunq",
            "handelsbanken",
            "ing",
            "knab",
            "moneyou",
            "n26",
            "nn",
            "rabobank",
            "regiobank",
            "revolut",
            "sns_bank",
            "triodos_bank",
            "van_lanschot",
            "yoursafe",
        ]
    ]


class _SerializerPaymentMethodCreateBodyIdeal(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyIdeal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank: typing.Optional[
        typing_extensions.Literal[
            "abn_amro",
            "asn_bank",
            "bunq",
            "handelsbanken",
            "ing",
            "knab",
            "moneyou",
            "n26",
            "nn",
            "rabobank",
            "regiobank",
            "revolut",
            "sns_bank",
            "triodos_bank",
            "van_lanschot",
            "yoursafe",
        ]
    ] = pydantic.Field(alias="bank", default=None)
