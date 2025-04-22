import pydantic
import typing
import typing_extensions

from .terminal_configuration_update_body_tipping_obj0_aud import (
    TerminalConfigurationUpdateBodyTippingObj0Aud,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Aud,
)
from .terminal_configuration_update_body_tipping_obj0_cad import (
    TerminalConfigurationUpdateBodyTippingObj0Cad,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Cad,
)
from .terminal_configuration_update_body_tipping_obj0_chf import (
    TerminalConfigurationUpdateBodyTippingObj0Chf,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Chf,
)
from .terminal_configuration_update_body_tipping_obj0_czk import (
    TerminalConfigurationUpdateBodyTippingObj0Czk,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Czk,
)
from .terminal_configuration_update_body_tipping_obj0_dkk import (
    TerminalConfigurationUpdateBodyTippingObj0Dkk,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Dkk,
)
from .terminal_configuration_update_body_tipping_obj0_eur import (
    TerminalConfigurationUpdateBodyTippingObj0Eur,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Eur,
)
from .terminal_configuration_update_body_tipping_obj0_gbp import (
    TerminalConfigurationUpdateBodyTippingObj0Gbp,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Gbp,
)
from .terminal_configuration_update_body_tipping_obj0_hkd import (
    TerminalConfigurationUpdateBodyTippingObj0Hkd,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Hkd,
)
from .terminal_configuration_update_body_tipping_obj0_jpy import (
    TerminalConfigurationUpdateBodyTippingObj0Jpy,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Jpy,
)
from .terminal_configuration_update_body_tipping_obj0_myr import (
    TerminalConfigurationUpdateBodyTippingObj0Myr,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Myr,
)
from .terminal_configuration_update_body_tipping_obj0_nok import (
    TerminalConfigurationUpdateBodyTippingObj0Nok,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Nok,
)
from .terminal_configuration_update_body_tipping_obj0_nzd import (
    TerminalConfigurationUpdateBodyTippingObj0Nzd,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Nzd,
)
from .terminal_configuration_update_body_tipping_obj0_pln import (
    TerminalConfigurationUpdateBodyTippingObj0Pln,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Pln,
)
from .terminal_configuration_update_body_tipping_obj0_sek import (
    TerminalConfigurationUpdateBodyTippingObj0Sek,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Sek,
)
from .terminal_configuration_update_body_tipping_obj0_sgd import (
    TerminalConfigurationUpdateBodyTippingObj0Sgd,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Sgd,
)
from .terminal_configuration_update_body_tipping_obj0_usd import (
    TerminalConfigurationUpdateBodyTippingObj0Usd,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0Usd,
)


class TerminalConfigurationUpdateBodyTippingObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyTippingObj0
    """

    aud: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Aud]

    cad: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Cad]

    chf: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Chf]

    czk: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Czk]

    dkk: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Dkk]

    eur: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Eur]

    gbp: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Gbp]

    hkd: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Hkd]

    jpy: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Jpy]

    myr: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Myr]

    nok: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Nok]

    nzd: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Nzd]

    pln: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Pln]

    sek: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Sek]

    sgd: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Sgd]

    usd: typing_extensions.NotRequired[TerminalConfigurationUpdateBodyTippingObj0Usd]


class _SerializerTerminalConfigurationUpdateBodyTippingObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyTippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aud: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Aud] = (
        pydantic.Field(alias="aud", default=None)
    )
    cad: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Cad] = (
        pydantic.Field(alias="cad", default=None)
    )
    chf: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Chf] = (
        pydantic.Field(alias="chf", default=None)
    )
    czk: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Czk] = (
        pydantic.Field(alias="czk", default=None)
    )
    dkk: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Dkk] = (
        pydantic.Field(alias="dkk", default=None)
    )
    eur: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Eur] = (
        pydantic.Field(alias="eur", default=None)
    )
    gbp: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Gbp] = (
        pydantic.Field(alias="gbp", default=None)
    )
    hkd: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Hkd] = (
        pydantic.Field(alias="hkd", default=None)
    )
    jpy: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Jpy] = (
        pydantic.Field(alias="jpy", default=None)
    )
    myr: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Myr] = (
        pydantic.Field(alias="myr", default=None)
    )
    nok: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Nok] = (
        pydantic.Field(alias="nok", default=None)
    )
    nzd: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Nzd] = (
        pydantic.Field(alias="nzd", default=None)
    )
    pln: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Pln] = (
        pydantic.Field(alias="pln", default=None)
    )
    sek: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Sek] = (
        pydantic.Field(alias="sek", default=None)
    )
    sgd: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Sgd] = (
        pydantic.Field(alias="sgd", default=None)
    )
    usd: typing.Optional[_SerializerTerminalConfigurationUpdateBodyTippingObj0Usd] = (
        pydantic.Field(alias="usd", default=None)
    )
