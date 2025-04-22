import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsIssuingCardFeatures(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsIssuingCardFeatures
    """

    card_management: typing_extensions.NotRequired[bool]

    card_spend_dispute_management: typing_extensions.NotRequired[bool]

    cardholder_management: typing_extensions.NotRequired[bool]

    spend_control_management: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsIssuingCardFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsIssuingCardFeatures handling case conversions
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
    spend_control_management: typing.Optional[bool] = pydantic.Field(
        alias="spend_control_management", default=None
    )
