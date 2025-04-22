import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quotes_resource_recurring import QuotesResourceRecurring
    from .quotes_resource_upfront import QuotesResourceUpfront


class QuotesResourceComputed(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    recurring: typing.Optional["QuotesResourceRecurring"] = pydantic.Field(
        alias="recurring", default=None
    )
    upfront: "QuotesResourceUpfront" = pydantic.Field(
        alias="upfront",
    )
