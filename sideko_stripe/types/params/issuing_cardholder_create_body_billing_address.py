import pydantic
import typing
import typing_extensions


class IssuingCardholderCreateBodyBillingAddress(typing_extensions.TypedDict):
    """
    IssuingCardholderCreateBodyBillingAddress
    """

    city: typing_extensions.Required[str]

    country: typing_extensions.Required[str]

    line1: typing_extensions.Required[str]

    line2: typing_extensions.NotRequired[str]

    postal_code: typing_extensions.Required[str]

    state: typing_extensions.NotRequired[str]


class _SerializerIssuingCardholderCreateBodyBillingAddress(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyBillingAddress handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: str = pydantic.Field(
        alias="city",
    )
    country: str = pydantic.Field(
        alias="country",
    )
    line1: str = pydantic.Field(
        alias="line1",
    )
    line2: typing.Optional[str] = pydantic.Field(alias="line2", default=None)
    postal_code: str = pydantic.Field(
        alias="postal_code",
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
