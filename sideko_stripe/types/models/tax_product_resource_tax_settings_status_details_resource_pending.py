import pydantic
import typing


class TaxProductResourceTaxSettingsStatusDetailsResourcePending(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    missing_fields: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="missing_fields", default=None
    )
    """
    The list of missing fields that are required to perform calculations. It includes the entry `head_office` when the status is `pending`. It is recommended to set the optional values even if they aren't listed as required for calculating taxes. Calculations can fail if missing fields aren't explicitly provided on every call.
    """
