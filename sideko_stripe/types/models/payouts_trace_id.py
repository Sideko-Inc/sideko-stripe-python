import pydantic
import typing


class PayoutsTraceId(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: str = pydantic.Field(
        alias="status",
    )
    """
    Possible values are `pending`, `supported`, and `unsupported`. When `payout.status` is `pending` or `in_transit`, this will be `pending`. When the payout transitions to `paid`, `failed`, or `canceled`, this status will become `supported` or `unsupported` shortly after in most cases. In some cases, this may appear as `pending` for up to 10 days after `arrival_date` until transitioning to `supported` or `unsupported`.
    """
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    """
    The trace ID value if `trace_id.status` is `supported`, otherwise `nil`.
    """
