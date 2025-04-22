import pydantic
import typing
import typing_extensions


class UsBankAccountNetworks(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    preferred: typing.Optional[str] = pydantic.Field(alias="preferred", default=None)
    """
    The preferred network.
    """
    supported: typing.List[typing_extensions.Literal["ach", "us_domestic_wire"]] = (
        pydantic.Field(
            alias="supported",
        )
    )
    """
    All supported networks.
    """
