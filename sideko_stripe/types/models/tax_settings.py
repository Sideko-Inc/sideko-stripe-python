import pydantic
import typing
import typing_extensions

from .tax_product_resource_tax_settings_defaults import (
    TaxProductResourceTaxSettingsDefaults,
)
from .tax_product_resource_tax_settings_head_office import (
    TaxProductResourceTaxSettingsHeadOffice,
)
from .tax_product_resource_tax_settings_status_details import (
    TaxProductResourceTaxSettingsStatusDetails,
)


class TaxSettings(pydantic.BaseModel):
    """
    You can use Tax `Settings` to manage configurations used by Stripe Tax calculations.

    Related guide: [Using the Settings API](https://stripe.com/docs/tax/settings-api)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    defaults: TaxProductResourceTaxSettingsDefaults = pydantic.Field(
        alias="defaults",
    )
    head_office: typing.Optional[TaxProductResourceTaxSettingsHeadOffice] = (
        pydantic.Field(alias="head_office", default=None)
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["tax.settings"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "pending"] = pydantic.Field(
        alias="status",
    )
    """
    The status of the Tax `Settings`.
    """
    status_details: TaxProductResourceTaxSettingsStatusDetails = pydantic.Field(
        alias="status_details",
    )
