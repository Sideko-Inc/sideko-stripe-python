import pydantic
import typing
import typing_extensions


class TreasuryFinancialAccountsResourceClosedStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reasons: typing.List[
        typing_extensions.Literal["account_rejected", "closed_by_platform", "other"]
    ] = pydantic.Field(
        alias="reasons",
    )
    """
    The array that contains reasons for a FinancialAccount closure.
    """
