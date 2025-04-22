import pydantic
import typing
import typing_extensions

from .treasury_transaction_list_status_transitions_posted_at_obj0 import (
    TreasuryTransactionListStatusTransitionsPostedAtObj0,
    _SerializerTreasuryTransactionListStatusTransitionsPostedAtObj0,
)


class TreasuryTransactionListStatusTransitions(typing_extensions.TypedDict):
    """
    A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified.
    """

    posted_at: typing_extensions.NotRequired[
        typing.Union[TreasuryTransactionListStatusTransitionsPostedAtObj0, int]
    ]


class _SerializerTreasuryTransactionListStatusTransitions(pydantic.BaseModel):
    """
    Serializer for TreasuryTransactionListStatusTransitions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    posted_at: typing.Optional[
        typing.Union[
            _SerializerTreasuryTransactionListStatusTransitionsPostedAtObj0, int
        ]
    ] = pydantic.Field(alias="posted_at", default=None)
