import pydantic
import typing_extensions


class AccountUnificationAccountControllerLosses(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payments: typing_extensions.Literal["application", "stripe"] = pydantic.Field(
        alias="payments",
    )
    """
    A value indicating who is liable when this account can't pay back negative balances from payments.
    """
