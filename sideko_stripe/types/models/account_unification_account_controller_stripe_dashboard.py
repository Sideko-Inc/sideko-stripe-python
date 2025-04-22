import pydantic
import typing_extensions


class AccountUnificationAccountControllerStripeDashboard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["express", "full", "none"] = pydantic.Field(
        alias="type",
    )
    """
    A value indicating the Stripe dashboard this account has access to independent of the Connect application.
    """
