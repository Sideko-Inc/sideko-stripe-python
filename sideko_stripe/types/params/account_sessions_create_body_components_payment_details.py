import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_payment_details_features import (
    AccountSessionsCreateBodyComponentsPaymentDetailsFeatures,
    _SerializerAccountSessionsCreateBodyComponentsPaymentDetailsFeatures,
)


class AccountSessionsCreateBodyComponentsPaymentDetails(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsPaymentDetails
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsPaymentDetailsFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsPaymentDetails(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsPaymentDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPaymentDetailsFeatures
    ] = pydantic.Field(alias="features", default=None)
