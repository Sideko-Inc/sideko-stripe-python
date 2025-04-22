import pydantic
import typing_extensions


class TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
    """
    Type of registration in `country`.
    """
