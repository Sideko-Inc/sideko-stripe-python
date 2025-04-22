import pydantic
import typing
import typing_extensions

from .test_helper_treasury_inbound_transfers_fail_body_failure_details import (
    TestHelperTreasuryInboundTransfersFailBodyFailureDetails,
    _SerializerTestHelperTreasuryInboundTransfersFailBodyFailureDetails,
)


class TestHelperTreasuryInboundTransfersFailBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryInboundTransfersFailBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    failure_details: typing_extensions.NotRequired[
        TestHelperTreasuryInboundTransfersFailBodyFailureDetails
    ]
    """
    Details about a failed InboundTransfer.
    """


class _SerializerTestHelperTreasuryInboundTransfersFailBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryInboundTransfersFailBody handling case conversions
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
    failure_details: typing.Optional[
        _SerializerTestHelperTreasuryInboundTransfersFailBodyFailureDetails
    ] = pydantic.Field(alias="failure_details", default=None)
