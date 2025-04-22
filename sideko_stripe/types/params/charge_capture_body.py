import pydantic
import typing
import typing_extensions

from .charge_capture_body_transfer_data import (
    ChargeCaptureBodyTransferData,
    _SerializerChargeCaptureBodyTransferData,
)


class ChargeCaptureBody(typing_extensions.TypedDict, total=False):
    """
    ChargeCaptureBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The amount to capture, which must be less than or equal to the original amount.
    """

    application_fee: typing_extensions.NotRequired[int]
    """
    An application fee to add on to this charge.
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    An application fee amount to add on to this charge, which must be less than or equal to the original amount.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    receipt_email: typing_extensions.NotRequired[str]
    """
    The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    
    For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    """

    statement_descriptor_suffix: typing_extensions.NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    """

    transfer_data: typing_extensions.NotRequired[ChargeCaptureBodyTransferData]
    """
    An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """


class _SerializerChargeCaptureBody(pydantic.BaseModel):
    """
    Serializer for ChargeCaptureBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    application_fee: typing.Optional[int] = pydantic.Field(
        alias="application_fee", default=None
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[_SerializerChargeCaptureBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
