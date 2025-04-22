import pydantic
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataFpx(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataFpx
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


class _SerializerPaymentIntentCreateBodyPaymentMethodDataFpx(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataFpx handling case conversions
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
