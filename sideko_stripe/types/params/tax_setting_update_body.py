import pydantic
import typing
import typing_extensions

from .tax_setting_update_body_defaults import (
    TaxSettingUpdateBodyDefaults,
    _SerializerTaxSettingUpdateBodyDefaults,
)
from .tax_setting_update_body_head_office import (
    TaxSettingUpdateBodyHeadOffice,
    _SerializerTaxSettingUpdateBodyHeadOffice,
)


class TaxSettingUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TaxSettingUpdateBody
    """

    defaults: typing_extensions.NotRequired[TaxSettingUpdateBodyDefaults]
    """
    Default configuration to be used on Stripe Tax calculations.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    head_office: typing_extensions.NotRequired[TaxSettingUpdateBodyHeadOffice]
    """
    The place where your business is located.
    """


class _SerializerTaxSettingUpdateBody(pydantic.BaseModel):
    """
    Serializer for TaxSettingUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    defaults: typing.Optional[_SerializerTaxSettingUpdateBodyDefaults] = pydantic.Field(
        alias="defaults", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    head_office: typing.Optional[_SerializerTaxSettingUpdateBodyHeadOffice] = (
        pydantic.Field(alias="head_office", default=None)
    )
