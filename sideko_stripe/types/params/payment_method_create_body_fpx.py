import pydantic
import typing_extensions


class PaymentMethodCreateBodyFpx(typing_extensions.TypedDict):
    """
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    """

    bank: typing_extensions.Required[
        typing_extensions.Literal[
            "affin_bank",
            "agrobank",
            "alliance_bank",
            "ambank",
            "bank_islam",
            "bank_muamalat",
            "bank_of_china",
            "bank_rakyat",
            "bsn",
            "cimb",
            "deutsche_bank",
            "hong_leong_bank",
            "hsbc",
            "kfh",
            "maybank2e",
            "maybank2u",
            "ocbc",
            "pb_enterprise",
            "public_bank",
            "rhb",
            "standard_chartered",
            "uob",
        ]
    ]


class _SerializerPaymentMethodCreateBodyFpx(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyFpx handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank: typing_extensions.Literal[
        "affin_bank",
        "agrobank",
        "alliance_bank",
        "ambank",
        "bank_islam",
        "bank_muamalat",
        "bank_of_china",
        "bank_rakyat",
        "bsn",
        "cimb",
        "deutsche_bank",
        "hong_leong_bank",
        "hsbc",
        "kfh",
        "maybank2e",
        "maybank2u",
        "ocbc",
        "pb_enterprise",
        "public_bank",
        "rhb",
        "standard_chartered",
        "uob",
    ] = pydantic.Field(
        alias="bank",
    )
