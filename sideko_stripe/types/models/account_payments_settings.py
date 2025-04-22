import pydantic
import typing


class AccountPaymentsSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge.
    """
    statement_descriptor_kana: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_kana", default=None
    )
    """
    The Kana variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors).
    """
    statement_descriptor_kanji: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_kanji", default=None
    )
    """
    The Kanji variation of `statement_descriptor` used for charges in Japan. Japanese statement descriptors have [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors).
    """
