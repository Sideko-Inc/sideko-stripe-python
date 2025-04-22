import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_issuing_card_features import (
    AccountSessionsCreateBodyComponentsIssuingCardFeatures,
    _SerializerAccountSessionsCreateBodyComponentsIssuingCardFeatures,
)


class AccountSessionsCreateBodyComponentsIssuingCard(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsIssuingCard
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsIssuingCardFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsIssuingCard(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsIssuingCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsIssuingCardFeatures
    ] = pydantic.Field(alias="features", default=None)
