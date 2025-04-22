import pydantic
import typing

from .tax_product_registrations_resource_country_options_canada import (
    TaxProductRegistrationsResourceCountryOptionsCanada,
)
from .tax_product_registrations_resource_country_options_default import (
    TaxProductRegistrationsResourceCountryOptionsDefault,
)
from .tax_product_registrations_resource_country_options_default_inbound_goods import (
    TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods,
)
from .tax_product_registrations_resource_country_options_europe import (
    TaxProductRegistrationsResourceCountryOptionsEurope,
)
from .tax_product_registrations_resource_country_options_simplified import (
    TaxProductRegistrationsResourceCountryOptionsSimplified,
)
from .tax_product_registrations_resource_country_options_united_states import (
    TaxProductRegistrationsResourceCountryOptionsUnitedStates,
)


class TaxProductRegistrationsResourceCountryOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ae: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="ae", default=None)
    al: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="al", default=None)
    )
    am: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="am", default=None)
    )
    ao: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="ao", default=None)
    )
    at: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="at", default=None)
    )
    au: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="au", default=None)
    ba: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="ba", default=None)
    )
    bb: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="bb", default=None)
    )
    be: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="be", default=None)
    )
    bg: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="bg", default=None)
    )
    bh: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="bh", default=None)
    )
    bs: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="bs", default=None)
    )
    by: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="by", default=None)
    )
    ca: typing.Optional[TaxProductRegistrationsResourceCountryOptionsCanada] = (
        pydantic.Field(alias="ca", default=None)
    )
    cd: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="cd", default=None)
    )
    ch: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="ch", default=None)
    cl: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="cl", default=None)
    )
    co: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="co", default=None)
    )
    cr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="cr", default=None)
    )
    cy: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="cy", default=None)
    )
    cz: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="cz", default=None)
    )
    de: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="de", default=None)
    )
    dk: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="dk", default=None)
    )
    ec: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ec", default=None)
    )
    ee: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="ee", default=None)
    )
    eg: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="eg", default=None)
    )
    es: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="es", default=None)
    )
    fi: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="fi", default=None)
    )
    fr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="fr", default=None)
    )
    gb: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="gb", default=None)
    ge: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ge", default=None)
    )
    gn: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="gn", default=None)
    )
    gr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="gr", default=None)
    )
    hr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="hr", default=None)
    )
    hu: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="hu", default=None)
    )
    id: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="id", default=None)
    )
    ie: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="ie", default=None)
    )
    is_: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="is", default=None)
    )
    it: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="it", default=None)
    )
    jp: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="jp", default=None)
    ke: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ke", default=None)
    )
    kh: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="kh", default=None)
    )
    kr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="kr", default=None)
    )
    kz: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="kz", default=None)
    )
    lt: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="lt", default=None)
    )
    lu: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="lu", default=None)
    )
    lv: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="lv", default=None)
    )
    ma: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ma", default=None)
    )
    md: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="md", default=None)
    )
    me: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="me", default=None)
    )
    mk: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="mk", default=None)
    )
    mr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="mr", default=None)
    )
    mt: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="mt", default=None)
    )
    mx: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="mx", default=None)
    )
    my: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="my", default=None)
    )
    ng: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ng", default=None)
    )
    nl: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="nl", default=None)
    )
    no: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="no", default=None)
    np: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="np", default=None)
    )
    nz: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="nz", default=None)
    om: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="om", default=None)
    )
    pe: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="pe", default=None)
    )
    pl: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="pl", default=None)
    )
    pt: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="pt", default=None)
    )
    ro: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="ro", default=None)
    )
    rs: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="rs", default=None)
    )
    ru: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ru", default=None)
    )
    sa: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="sa", default=None)
    )
    se: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="se", default=None)
    )
    sg: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsDefaultInboundGoods
    ] = pydantic.Field(alias="sg", default=None)
    si: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="si", default=None)
    )
    sk: typing.Optional[TaxProductRegistrationsResourceCountryOptionsEurope] = (
        pydantic.Field(alias="sk", default=None)
    )
    sn: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="sn", default=None)
    )
    sr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="sr", default=None)
    )
    th: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="th", default=None)
    )
    tj: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="tj", default=None)
    )
    tr: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="tr", default=None)
    )
    tz: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="tz", default=None)
    )
    ug: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="ug", default=None)
    )
    us: typing.Optional[TaxProductRegistrationsResourceCountryOptionsUnitedStates] = (
        pydantic.Field(alias="us", default=None)
    )
    uy: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="uy", default=None)
    )
    uz: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="uz", default=None)
    )
    vn: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="vn", default=None)
    )
    za: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="za", default=None)
    )
    zm: typing.Optional[TaxProductRegistrationsResourceCountryOptionsSimplified] = (
        pydantic.Field(alias="zm", default=None)
    )
    zw: typing.Optional[TaxProductRegistrationsResourceCountryOptionsDefault] = (
        pydantic.Field(alias="zw", default=None)
    )
