import pydantic
import typing
import typing_extensions


class TaxIdVerification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal[
        "pending", "unavailable", "unverified", "verified"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Verification status, one of `pending`, `verified`, `unverified`, or `unavailable`.
    """
    verified_address: typing.Optional[str] = pydantic.Field(
        alias="verified_address", default=None
    )
    """
    Verified address.
    """
    verified_name: typing.Optional[str] = pydantic.Field(
        alias="verified_name", default=None
    )
    """
    Verified name.
    """
