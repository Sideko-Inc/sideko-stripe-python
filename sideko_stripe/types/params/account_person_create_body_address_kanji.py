import pydantic
import typing
import typing_extensions


class AccountPersonCreateBodyAddressKanji(typing_extensions.TypedDict):
    """
    The Kanji variation of the person's address (Japan only).
    """

    city: typing_extensions.NotRequired[str]

    country: typing_extensions.NotRequired[str]

    line1: typing_extensions.NotRequired[str]

    line2: typing_extensions.NotRequired[str]

    postal_code: typing_extensions.NotRequired[str]

    state: typing_extensions.NotRequired[str]

    town: typing_extensions.NotRequired[str]


class _SerializerAccountPersonCreateBodyAddressKanji(pydantic.BaseModel):
    """
    Serializer for AccountPersonCreateBodyAddressKanji handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    line1: typing.Optional[str] = pydantic.Field(alias="line1", default=None)
    line2: typing.Optional[str] = pydantic.Field(alias="line2", default=None)
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    town: typing.Optional[str] = pydantic.Field(alias="town", default=None)
