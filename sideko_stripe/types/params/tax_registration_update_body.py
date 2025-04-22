import pydantic
import typing
import typing_extensions


class TaxRegistrationUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TaxRegistrationUpdateBody
    """

    active_from: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int]
    ]
    """
    Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int, str]
    ]
    """
    If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
    """


class _SerializerTaxRegistrationUpdateBody(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active_from: typing.Optional[
        typing.Union[typing_extensions.Literal["now"], int]
    ] = pydantic.Field(alias="active_from", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[
        typing.Union[typing_extensions.Literal["now"], int, str]
    ] = pydantic.Field(alias="expires_at", default=None)
