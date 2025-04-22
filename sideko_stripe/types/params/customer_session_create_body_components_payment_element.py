import pydantic
import typing
import typing_extensions

from .customer_session_create_body_components_payment_element_features import (
    CustomerSessionCreateBodyComponentsPaymentElementFeatures,
    _SerializerCustomerSessionCreateBodyComponentsPaymentElementFeatures,
)


class CustomerSessionCreateBodyComponentsPaymentElement(typing_extensions.TypedDict):
    """
    CustomerSessionCreateBodyComponentsPaymentElement
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        CustomerSessionCreateBodyComponentsPaymentElementFeatures
    ]


class _SerializerCustomerSessionCreateBodyComponentsPaymentElement(pydantic.BaseModel):
    """
    Serializer for CustomerSessionCreateBodyComponentsPaymentElement handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerCustomerSessionCreateBodyComponentsPaymentElementFeatures
    ] = pydantic.Field(alias="features", default=None)
