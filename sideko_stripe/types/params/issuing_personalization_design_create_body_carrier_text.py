import pydantic
import typing
import typing_extensions


class IssuingPersonalizationDesignCreateBodyCarrierText(typing_extensions.TypedDict):
    """
    Hash containing carrier text, for use with physical bundles that support carrier text.
    """

    footer_body: typing_extensions.NotRequired[typing.Union[str, str]]

    footer_title: typing_extensions.NotRequired[typing.Union[str, str]]

    header_body: typing_extensions.NotRequired[typing.Union[str, str]]

    header_title: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerIssuingPersonalizationDesignCreateBodyCarrierText(pydantic.BaseModel):
    """
    Serializer for IssuingPersonalizationDesignCreateBodyCarrierText handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    footer_body: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="footer_body", default=None
    )
    footer_title: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="footer_title", default=None
    )
    header_body: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="header_body", default=None
    )
    header_title: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="header_title", default=None
    )
