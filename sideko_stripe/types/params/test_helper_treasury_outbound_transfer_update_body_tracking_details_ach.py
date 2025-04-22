import pydantic
import typing_extensions


class TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch(
    typing_extensions.TypedDict
):
    """
    TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch
    """

    trace_id: typing_extensions.Required[str]


class _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    trace_id: str = pydantic.Field(
        alias="trace_id",
    )
