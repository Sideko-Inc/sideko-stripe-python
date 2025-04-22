import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options import (
    TaxRegistrationCreateBodyCountryOptions,
    _SerializerTaxRegistrationCreateBodyCountryOptions,
)


class TaxRegistrationCreateBody(typing_extensions.TypedDict, total=False):
    """
    TaxRegistrationCreateBody
    """

    active_from: typing_extensions.Required[
        typing.Union[typing_extensions.Literal["now"], int]
    ]
    """
    Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
    """

    country: typing_extensions.Required[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    country_options: typing_extensions.Required[TaxRegistrationCreateBodyCountryOptions]
    """
    Specific options for a registration in the specified `country`.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.
    """


class _SerializerTaxRegistrationCreateBody(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active_from: typing.Union[typing_extensions.Literal["now"], int] = pydantic.Field(
        alias="active_from",
    )
    country: str = pydantic.Field(
        alias="country",
    )
    country_options: _SerializerTaxRegistrationCreateBodyCountryOptions = (
        pydantic.Field(
            alias="country_options",
        )
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
