import pydantic
import typing
import typing_extensions


class TreasuryReceivedDebitsResourceReversalDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deadline: typing.Optional[int] = pydantic.Field(alias="deadline", default=None)
    """
    Time before which a ReceivedDebit can be reversed.
    """
    restricted_reason: typing.Optional[
        typing_extensions.Literal[
            "already_reversed",
            "deadline_passed",
            "network_restricted",
            "other",
            "source_flow_restricted",
        ]
    ] = pydantic.Field(alias="restricted_reason", default=None)
    """
    Set if a ReceivedDebit can't be reversed.
    """
