import pydantic
import typing
import typing_extensions


class AccountUpdateBodySettingsPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsPayments
    """

    statement_descriptor: typing_extensions.NotRequired[str]

    statement_descriptor_kana: typing_extensions.NotRequired[str]

    statement_descriptor_kanji: typing_extensions.NotRequired[str]


class _SerializerAccountUpdateBodySettingsPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_kana: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_kana", default=None
    )
    statement_descriptor_kanji: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_kanji", default=None
    )
