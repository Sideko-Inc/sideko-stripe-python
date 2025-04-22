import pydantic
import typing
import typing_extensions

from .tax_product_registrations_resource_country_options import (
    TaxProductRegistrationsResourceCountryOptions,
)


class TaxRegistration(pydantic.BaseModel):
    """
    A Tax `Registration` lets us know that your business is registered to collect tax on payments within a region, enabling you to [automatically collect tax](https://stripe.com/docs/tax).

    Stripe doesn't register on your behalf with the relevant authorities when you create a Tax `Registration` object. For more information on how to register to collect tax, see [our guide](https://stripe.com/docs/tax/registering).

    Related guide: [Using the Registrations API](https://stripe.com/docs/tax/registrations-api)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active_from: int = pydantic.Field(
        alias="active_from",
    )
    """
    Time at which the registration becomes active. Measured in seconds since the Unix epoch.
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    country_options: TaxProductRegistrationsResourceCountryOptions = pydantic.Field(
        alias="country_options",
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["tax.registration"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "expired", "scheduled"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the registration. This field is present for convenience and can be deduced from `active_from` and `expires_at`.
    """
