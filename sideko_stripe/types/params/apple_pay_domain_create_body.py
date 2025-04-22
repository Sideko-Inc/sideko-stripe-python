import pydantic
import typing
import typing_extensions


class ApplePayDomainCreateBody(typing_extensions.TypedDict, total=False):
    """
    ApplePayDomainCreateBody
    """

    domain_name: typing_extensions.Required[str]

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerApplePayDomainCreateBody(pydantic.BaseModel):
    """
    Serializer for ApplePayDomainCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    domain_name: str = pydantic.Field(
        alias="domain_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
