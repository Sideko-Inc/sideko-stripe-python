import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .customer import Customer


class ThresholdsResourceUsageAlertFilter(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer: typing.Optional[typing.Union[str, "Customer"]] = pydantic.Field(
        alias="customer", default=None
    )
    """
    Limit the scope of the alert to this customer ID
    """
    type_: typing_extensions.Literal["customer"] = pydantic.Field(
        alias="type",
    )
