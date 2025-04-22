import pydantic
import typing
import typing_extensions


class PaymentMethodIdeal(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
    """
    The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.
    """
    bic: typing.Optional[
        typing_extensions.Literal[
            "ABNANL2A",
            "ASNBNL21",
            "BITSNL2A",
            "BUNQNL2A",
            "FVLBNL22",
            "HANDNL2A",
            "INGBNL2A",
            "KNABNL2H",
            "MOYONL21",
            "NNBANL2G",
            "NTSBDEB1",
            "RABONL2U",
            "RBRBNL21",
            "REVOIE23",
            "REVOLT21",
            "SNSBNL2A",
            "TRIONL2U",
        ]
    ] = pydantic.Field(alias="bic", default=None)
    """
    The Bank Identifier Code of the customer's bank, if the bank was provided.
    """
