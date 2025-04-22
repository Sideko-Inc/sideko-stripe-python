import pydantic
import typing
import typing_extensions


class TokenCreateBodyCardObj0Networks(typing_extensions.TypedDict):
    """
    TokenCreateBodyCardObj0Networks
    """

    preferred: typing_extensions.NotRequired[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ]


class _SerializerTokenCreateBodyCardObj0Networks(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyCardObj0Networks handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preferred: typing.Optional[
        typing_extensions.Literal["cartes_bancaires", "mastercard", "visa"]
    ] = pydantic.Field(alias="preferred", default=None)
