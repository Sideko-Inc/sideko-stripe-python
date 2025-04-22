import pydantic
import typing
import typing_extensions

from .billing_credit_grant_update_body_metadata import (
    BillingCreditGrantUpdateBodyMetadata,
    _SerializerBillingCreditGrantUpdateBodyMetadata,
)


class BillingCreditGrantUpdateBody(typing_extensions.TypedDict, total=False):
    """
    BillingCreditGrantUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[typing.Union[int, str]]
    """
    The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.
    """

    metadata: typing_extensions.NotRequired[BillingCreditGrantUpdateBodyMetadata]
    """
    Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
    """


class _SerializerBillingCreditGrantUpdateBody(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="expires_at", default=None
    )
    metadata: typing.Optional[_SerializerBillingCreditGrantUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
