import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_issuing_cards_list_features import (
    AccountSessionsCreateBodyComponentsIssuingCardsListFeatures,
    _SerializerAccountSessionsCreateBodyComponentsIssuingCardsListFeatures,
)


class AccountSessionsCreateBodyComponentsIssuingCardsList(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsIssuingCardsList
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsIssuingCardsListFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsIssuingCardsList(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsIssuingCardsList handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsIssuingCardsListFeatures
    ] = pydantic.Field(alias="features", default=None)
