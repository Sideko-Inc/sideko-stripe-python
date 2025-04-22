import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsIssuingCardsListFeatures(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsIssuingCardsListFeatures
    """

    card_management: typing_extensions.NotRequired[bool]

    card_spend_dispute_management: typing_extensions.NotRequired[bool]

    cardholder_management: typing_extensions.NotRequired[bool]

    disable_stripe_user_authentication: typing_extensions.NotRequired[bool]

    spend_control_management: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsIssuingCardsListFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsIssuingCardsListFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_management: typing.Optional[bool] = pydantic.Field(
        alias="card_management", default=None
    )
    card_spend_dispute_management: typing.Optional[bool] = pydantic.Field(
        alias="card_spend_dispute_management", default=None
    )
    cardholder_management: typing.Optional[bool] = pydantic.Field(
        alias="cardholder_management", default=None
    )
    disable_stripe_user_authentication: typing.Optional[bool] = pydantic.Field(
        alias="disable_stripe_user_authentication", default=None
    )
    spend_control_management: typing.Optional[bool] = pydantic.Field(
        alias="spend_control_management", default=None
    )
