import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsP24(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank: typing.Optional[
        typing_extensions.Literal[
            "alior_bank",
            "bank_millennium",
            "bank_nowy_bfg_sa",
            "bank_pekao_sa",
            "banki_spbdzielcze",
            "blik",
            "bnp_paribas",
            "boz",
            "citi_handlowy",
            "credit_agricole",
            "envelobank",
            "etransfer_pocztowy24",
            "getin_bank",
            "ideabank",
            "ing",
            "inteligo",
            "mbank_mtransfer",
            "nest_przelew",
            "noble_pay",
            "pbac_z_ipko",
            "plus_bank",
            "santander_przelew24",
            "tmobile_usbugi_bankowe",
            "toyota_bank",
            "velobank",
            "volkswagen_bank",
        ]
    ] = pydantic.Field(alias="bank", default=None)
    """
    The customer's bank. Can be one of `ing`, `citi_handlowy`, `tmobile_usbugi_bankowe`, `plus_bank`, `etransfer_pocztowy24`, `banki_spbdzielcze`, `bank_nowy_bfg_sa`, `getin_bank`, `velobank`, `blik`, `noble_pay`, `ideabank`, `envelobank`, `santander_przelew24`, `nest_przelew`, `mbank_mtransfer`, `inteligo`, `pbac_z_ipko`, `bnp_paribas`, `credit_agricole`, `toyota_bank`, `bank_pekao_sa`, `volkswagen_bank`, `bank_millennium`, `alior_bank`, or `boz`.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Unique reference for this Przelewy24 payment.
    """
    verified_name: typing.Optional[str] = pydantic.Field(
        alias="verified_name", default=None
    )
    """
    Owner's verified full name. Values are verified or provided by Przelewy24 directly
    (if supported) at the time of authorization or settlement. They cannot be set or mutated.
    Przelewy24 rarely provides this information so the attribute is usually empty.
    """
