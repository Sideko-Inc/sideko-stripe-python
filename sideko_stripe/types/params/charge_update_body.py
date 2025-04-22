import pydantic
import typing
import typing_extensions

from .charge_update_body_fraud_details import (
    ChargeUpdateBodyFraudDetails,
    _SerializerChargeUpdateBodyFraudDetails,
)
from .charge_update_body_metadata_obj0 import (
    ChargeUpdateBodyMetadataObj0,
    _SerializerChargeUpdateBodyMetadataObj0,
)
from .charge_update_body_shipping import (
    ChargeUpdateBodyShipping,
    _SerializerChargeUpdateBodyShipping,
)


class ChargeUpdateBody(typing_extensions.TypedDict, total=False):
    """
    ChargeUpdateBody
    """

    customer: typing_extensions.NotRequired[str]
    """
    The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fraud_details: typing_extensions.NotRequired[ChargeUpdateBodyFraudDetails]
    """
    A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ChargeUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    receipt_email: typing_extensions.NotRequired[str]
    """
    This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
    """

    shipping: typing_extensions.NotRequired[ChargeUpdateBodyShipping]
    """
    Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """


class _SerializerChargeUpdateBody(pydantic.BaseModel):
    """
    Serializer for ChargeUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fraud_details: typing.Optional[_SerializerChargeUpdateBodyFraudDetails] = (
        pydantic.Field(alias="fraud_details", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerChargeUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    shipping: typing.Optional[_SerializerChargeUpdateBodyShipping] = pydantic.Field(
        alias="shipping", default=None
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
