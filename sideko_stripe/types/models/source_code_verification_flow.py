import pydantic


class SourceCodeVerificationFlow(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attempts_remaining: int = pydantic.Field(
        alias="attempts_remaining",
    )
    """
    The number of attempts remaining to authenticate the source object with a verification code.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0).
    """
