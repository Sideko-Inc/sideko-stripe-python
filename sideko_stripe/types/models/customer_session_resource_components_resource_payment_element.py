import pydantic
import typing

from .customer_session_resource_components_resource_payment_element_resource_features import (
    CustomerSessionResourceComponentsResourcePaymentElementResourceFeatures,
)


class CustomerSessionResourceComponentsResourcePaymentElement(pydantic.BaseModel):
    """
    This hash contains whether the Payment Element is enabled and the features it supports.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the Payment Element is enabled.
    """
    features: typing.Optional[
        CustomerSessionResourceComponentsResourcePaymentElementResourceFeatures
    ] = pydantic.Field(alias="features", default=None)
    """
    This hash contains the features the Payment Element supports.
    """
