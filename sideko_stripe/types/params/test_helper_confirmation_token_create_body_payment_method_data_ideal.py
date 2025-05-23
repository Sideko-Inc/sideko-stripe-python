import pydantic
import typing
import typing_extensions


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataIdeal(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataIdeal
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


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataIdeal(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataIdeal handling case conversions
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
