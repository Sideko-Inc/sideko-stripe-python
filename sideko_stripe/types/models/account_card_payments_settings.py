import pydantic
import typing

from .account_decline_charge_on import AccountDeclineChargeOn


class AccountCardPaymentsSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    decline_on: typing.Optional[AccountDeclineChargeOn] = pydantic.Field(
        alias="decline_on", default=None
    )
    statement_descriptor_prefix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_prefix", default=None
    )
    """
    The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion.
    """
    statement_descriptor_prefix_kana: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_prefix_kana", default=None
    )
    """
    The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion.
    """
    statement_descriptor_prefix_kanji: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_prefix_kanji", default=None
    )
    """
    The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion.
    """
