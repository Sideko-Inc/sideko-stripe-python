import pydantic
import typing_extensions


class TokenCreateBodyCvcUpdate(typing_extensions.TypedDict):
    """
    The updated CVC value this token represents.
    """

    cvc: typing_extensions.Required[str]


class _SerializerTokenCreateBodyCvcUpdate(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyCvcUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cvc: str = pydantic.Field(
        alias="cvc",
    )
