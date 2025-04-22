import pydantic
import typing
import typing_extensions

from .issuing_cardholder_update_body_billing import (
    IssuingCardholderUpdateBodyBilling,
    _SerializerIssuingCardholderUpdateBodyBilling,
)
from .issuing_cardholder_update_body_company import (
    IssuingCardholderUpdateBodyCompany,
    _SerializerIssuingCardholderUpdateBodyCompany,
)
from .issuing_cardholder_update_body_individual import (
    IssuingCardholderUpdateBodyIndividual,
    _SerializerIssuingCardholderUpdateBodyIndividual,
)
from .issuing_cardholder_update_body_metadata import (
    IssuingCardholderUpdateBodyMetadata,
    _SerializerIssuingCardholderUpdateBodyMetadata,
)
from .issuing_cardholder_update_body_spending_controls import (
    IssuingCardholderUpdateBodySpendingControls,
    _SerializerIssuingCardholderUpdateBodySpendingControls,
)


class IssuingCardholderUpdateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingCardholderUpdateBody
    """

    billing: typing_extensions.NotRequired[IssuingCardholderUpdateBodyBilling]
    """
    The cardholder's billing address.
    """

    company: typing_extensions.NotRequired[IssuingCardholderUpdateBodyCompany]
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

    individual: typing_extensions.NotRequired[IssuingCardholderUpdateBodyIndividual]
    """
    Additional information about an `individual` cardholder.
    """

    metadata: typing_extensions.NotRequired[IssuingCardholderUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    phone_number: typing_extensions.NotRequired[str]
    """
    The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure) for more details.
    """

    preferred_locales: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
    ]
    """
    The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
     This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
    """

    spending_controls: typing_extensions.NotRequired[
        IssuingCardholderUpdateBodySpendingControls
    ]
    """
    Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["active", "inactive"]
    ]
    """
    Specifies whether to permit authorizations on this cardholder's cards.
    """


class _SerializerIssuingCardholderUpdateBody(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    billing: typing.Optional[_SerializerIssuingCardholderUpdateBodyBilling] = (
        pydantic.Field(alias="billing", default=None)
    )
    company: typing.Optional[_SerializerIssuingCardholderUpdateBodyCompany] = (
        pydantic.Field(alias="company", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    individual: typing.Optional[_SerializerIssuingCardholderUpdateBodyIndividual] = (
        pydantic.Field(alias="individual", default=None)
    )
    metadata: typing.Optional[_SerializerIssuingCardholderUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    preferred_locales: typing.Optional[
        typing.List[typing_extensions.Literal["de", "en", "es", "fr", "it"]]
    ] = pydantic.Field(alias="preferred_locales", default=None)
    spending_controls: typing.Optional[
        _SerializerIssuingCardholderUpdateBodySpendingControls
    ] = pydantic.Field(alias="spending_controls", default=None)
    status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="status", default=None)
    )
