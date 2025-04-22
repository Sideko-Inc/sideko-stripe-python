import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_transfer_returned_body_returned_details import (
    TestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails,
    _SerializerTestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails,
)


class TestHelperTreasuryOutboundTransferReturnedBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryOutboundTransferReturnedBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    returned_details: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails
    ]
    """
    Details about a returned OutboundTransfer.
    """


class _SerializerTestHelperTreasuryOutboundTransferReturnedBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryOutboundTransferReturnedBody handling case conversions
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
    returned_details: typing.Optional[
        _SerializerTestHelperTreasuryOutboundTransferReturnedBodyReturnedDetails
    ] = pydantic.Field(alias="returned_details", default=None)
