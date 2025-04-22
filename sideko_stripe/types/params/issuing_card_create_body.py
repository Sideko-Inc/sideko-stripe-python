import pydantic
import typing
import typing_extensions

from .issuing_card_create_body_metadata import (
    IssuingCardCreateBodyMetadata,
    _SerializerIssuingCardCreateBodyMetadata,
)
from .issuing_card_create_body_pin import (
    IssuingCardCreateBodyPin,
    _SerializerIssuingCardCreateBodyPin,
)
from .issuing_card_create_body_shipping import (
    IssuingCardCreateBodyShipping,
    _SerializerIssuingCardCreateBodyShipping,
)
from .issuing_card_create_body_spending_controls import (
    IssuingCardCreateBodySpendingControls,
    _SerializerIssuingCardCreateBodySpendingControls,
)


class IssuingCardCreateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingCardCreateBody
    """

    cardholder: typing_extensions.NotRequired[str]
    """
    The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated.
    """

    currency: typing_extensions.Required[str]
    """
    The currency for the card.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_account: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[IssuingCardCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    personalization_design: typing_extensions.NotRequired[str]
    """
    The personalization design object belonging to this card.
    """

    pin: typing_extensions.NotRequired[IssuingCardCreateBodyPin]
    """
    The desired PIN for this card.
    """

    replacement_for: typing_extensions.NotRequired[str]
    """
    The card this is meant to be a replacement for (if any).
    """

    replacement_reason: typing_extensions.NotRequired[
        typing_extensions.Literal["damaged", "expired", "lost", "stolen"]
    ]
    """
    If `replacement_for` is specified, this should indicate why that card is being replaced.
    """

    second_line: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The second line to print on the card. Max length: 24 characters.
    """

    shipping: typing_extensions.NotRequired[IssuingCardCreateBodyShipping]
    """
    The address where the card will be shipped.
    """

    spending_controls: typing_extensions.NotRequired[
        IssuingCardCreateBodySpendingControls
    ]
    """
    Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["active", "inactive"]
    ]
    """
    Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["physical", "virtual"]]
    """
    The type of card to issue. Possible values are `physical` or `virtual`.
    """


class _SerializerIssuingCardCreateBody(pydantic.BaseModel):
    """
    Serializer for IssuingCardCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cardholder: typing.Optional[str] = pydantic.Field(alias="cardholder", default=None)
    currency: str = pydantic.Field(
        alias="currency",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    metadata: typing.Optional[_SerializerIssuingCardCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    personalization_design: typing.Optional[str] = pydantic.Field(
        alias="personalization_design", default=None
    )
    pin: typing.Optional[_SerializerIssuingCardCreateBodyPin] = pydantic.Field(
        alias="pin", default=None
    )
    replacement_for: typing.Optional[str] = pydantic.Field(
        alias="replacement_for", default=None
    )
    replacement_reason: typing.Optional[
        typing_extensions.Literal["damaged", "expired", "lost", "stolen"]
    ] = pydantic.Field(alias="replacement_reason", default=None)
    second_line: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="second_line", default=None
    )
    shipping: typing.Optional[_SerializerIssuingCardCreateBodyShipping] = (
        pydantic.Field(alias="shipping", default=None)
    )
    spending_controls: typing.Optional[
        _SerializerIssuingCardCreateBodySpendingControls
    ] = pydantic.Field(alias="spending_controls", default=None)
    status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="status", default=None)
    )
    type_: typing_extensions.Literal["physical", "virtual"] = pydantic.Field(
        alias="type",
    )
