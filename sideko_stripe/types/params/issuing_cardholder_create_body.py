import pydantic
import typing
import typing_extensions

from .issuing_cardholder_create_body_billing import (
    IssuingCardholderCreateBodyBilling,
    _SerializerIssuingCardholderCreateBodyBilling,
)
from .issuing_cardholder_create_body_company import (
    IssuingCardholderCreateBodyCompany,
    _SerializerIssuingCardholderCreateBodyCompany,
)
from .issuing_cardholder_create_body_individual import (
    IssuingCardholderCreateBodyIndividual,
    _SerializerIssuingCardholderCreateBodyIndividual,
)
from .issuing_cardholder_create_body_metadata import (
    IssuingCardholderCreateBodyMetadata,
    _SerializerIssuingCardholderCreateBodyMetadata,
)
from .issuing_cardholder_create_body_spending_controls import (
    IssuingCardholderCreateBodySpendingControls,
    _SerializerIssuingCardholderCreateBodySpendingControls,
)


class IssuingCardholderCreateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingCardholderCreateBody
    """

    billing: typing_extensions.Required[IssuingCardholderCreateBodyBilling]
    """
    The cardholder's billing address.
    """

    company: typing_extensions.NotRequired[IssuingCardholderCreateBodyCompany]
    """
    Additional information about a `company` cardholder.
    """

    email: typing_extensions.NotRequired[str]
    """
    The cardholder's email address.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    individual: typing_extensions.NotRequired[IssuingCardholderCreateBodyIndividual]
    """
    Additional information about an `individual` cardholder.
    """

    metadata: typing_extensions.NotRequired[IssuingCardholderCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.Required[str]
    """
    The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.
    """

    phone_number: typing_extensions.NotRequired[str]
    """
    The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details.
    """

    preferred_locales: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
    ]
    """
    The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
     This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
    """

    spending_controls: typing_extensions.NotRequired[
        IssuingCardholderCreateBodySpendingControls
    ]
    """
    Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["active", "inactive"]
    ]
    """
    Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`.
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]
    """
    One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details.
    """


class _SerializerIssuingCardholderCreateBody(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    billing: _SerializerIssuingCardholderCreateBodyBilling = pydantic.Field(
        alias="billing",
    )
    company: typing.Optional[_SerializerIssuingCardholderCreateBodyCompany] = (
        pydantic.Field(alias="company", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    individual: typing.Optional[_SerializerIssuingCardholderCreateBodyIndividual] = (
        pydantic.Field(alias="individual", default=None)
    )
    metadata: typing.Optional[_SerializerIssuingCardholderCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    preferred_locales: typing.Optional[
        typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
    ] = pydantic.Field(alias="preferred_locales", default=None)
    spending_controls: typing.Optional[
        _SerializerIssuingCardholderCreateBodySpendingControls
    ] = pydantic.Field(alias="spending_controls", default=None)
    status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="status", default=None)
    )
    type_: typing.Optional[typing_extensions.Literal["company", "individual"]] = (
        pydantic.Field(alias="type", default=None)
    )
