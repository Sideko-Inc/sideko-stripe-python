import pydantic
import typing_extensions

from .tax_setting_update_body_head_office_address import (
    TaxSettingUpdateBodyHeadOfficeAddress,
    _SerializerTaxSettingUpdateBodyHeadOfficeAddress,
)


class TaxSettingUpdateBodyHeadOffice(typing_extensions.TypedDict):
    """
    The place where your business is located.
    """

    address: typing_extensions.Required[TaxSettingUpdateBodyHeadOfficeAddress]


class _SerializerTaxSettingUpdateBodyHeadOffice(pydantic.BaseModel):
    """
    Serializer for TaxSettingUpdateBodyHeadOffice handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerTaxSettingUpdateBodyHeadOfficeAddress = pydantic.Field(
        alias="address",
    )
