import pydantic
import typing_extensions


class IssuingAuthorizationThreeDSecure(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    result: typing_extensions.Literal[
        "attempt_acknowledged", "authenticated", "failed", "required"
    ] = pydantic.Field(
        alias="result",
    )
    """
    The outcome of the 3D Secure authentication request.
    """
