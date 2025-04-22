import pydantic
import typing
import typing_extensions

from .issuing_card_update_body_metadata_obj0 import (
    IssuingCardUpdateBodyMetadataObj0,
    _SerializerIssuingCardUpdateBodyMetadataObj0,
)
from .issuing_card_update_body_pin import (
    IssuingCardUpdateBodyPin,
    _SerializerIssuingCardUpdateBodyPin,
)
from .issuing_card_update_body_shipping import (
    IssuingCardUpdateBodyShipping,
    _SerializerIssuingCardUpdateBodyShipping,
)
from .issuing_card_update_body_spending_controls import (
    IssuingCardUpdateBodySpendingControls,
    _SerializerIssuingCardUpdateBodySpendingControls,
)


class IssuingCardUpdateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingCardUpdateBody
    """

    cancellation_reason: typing_extensions.NotRequired[
        typing_extensions.Literal["lost", "stolen"]
    ]
    """
    Reason why the `status` of this card is `canceled`.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[IssuingCardUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    personalization_design: typing_extensions.NotRequired[str]

    pin: typing_extensions.NotRequired[IssuingCardUpdateBodyPin]
    """
    The desired new PIN for this card.
    """

    shipping: typing_extensions.NotRequired[IssuingCardUpdateBodyShipping]
    """
    Updated shipping information for the card.
    """

    spending_controls: typing_extensions.NotRequired[
        IssuingCardUpdateBodySpendingControls
    ]
    """
    Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["active", "canceled", "inactive"]
    ]
    """
    Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. If this card is being canceled because it was lost or stolen, this information should be provided as `cancellation_reason`.
    """


class _SerializerIssuingCardUpdateBody(pydantic.BaseModel):
    """
    Serializer for IssuingCardUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cancellation_reason: typing.Optional[
        typing_extensions.Literal["lost", "stolen"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerIssuingCardUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    personalization_design: typing.Optional[str] = pydantic.Field(
        alias="personalization_design", default=None
    )
    pin: typing.Optional[_SerializerIssuingCardUpdateBodyPin] = pydantic.Field(
        alias="pin", default=None
    )
    shipping: typing.Optional[_SerializerIssuingCardUpdateBodyShipping] = (
        pydantic.Field(alias="shipping", default=None)
    )
    spending_controls: typing.Optional[
        _SerializerIssuingCardUpdateBodySpendingControls
    ] = pydantic.Field(alias="spending_controls", default=None)
    status: typing.Optional[
        typing_extensions.Literal["active", "canceled", "inactive"]
    ] = pydantic.Field(alias="status", default=None)
