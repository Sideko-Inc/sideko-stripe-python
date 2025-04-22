import pydantic
import typing
import typing_extensions

from .terminal_configuration_create_body_tipping_obj0_aud import (
    TerminalConfigurationCreateBodyTippingObj0Aud,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Aud,
)
from .terminal_configuration_create_body_tipping_obj0_cad import (
    TerminalConfigurationCreateBodyTippingObj0Cad,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Cad,
)
from .terminal_configuration_create_body_tipping_obj0_chf import (
    TerminalConfigurationCreateBodyTippingObj0Chf,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Chf,
)
from .terminal_configuration_create_body_tipping_obj0_czk import (
    TerminalConfigurationCreateBodyTippingObj0Czk,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Czk,
)
from .terminal_configuration_create_body_tipping_obj0_dkk import (
    TerminalConfigurationCreateBodyTippingObj0Dkk,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Dkk,
)
from .terminal_configuration_create_body_tipping_obj0_eur import (
    TerminalConfigurationCreateBodyTippingObj0Eur,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Eur,
)
from .terminal_configuration_create_body_tipping_obj0_gbp import (
    TerminalConfigurationCreateBodyTippingObj0Gbp,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Gbp,
)
from .terminal_configuration_create_body_tipping_obj0_hkd import (
    TerminalConfigurationCreateBodyTippingObj0Hkd,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Hkd,
)
from .terminal_configuration_create_body_tipping_obj0_jpy import (
    TerminalConfigurationCreateBodyTippingObj0Jpy,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Jpy,
)
from .terminal_configuration_create_body_tipping_obj0_myr import (
    TerminalConfigurationCreateBodyTippingObj0Myr,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Myr,
)
from .terminal_configuration_create_body_tipping_obj0_nok import (
    TerminalConfigurationCreateBodyTippingObj0Nok,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Nok,
)
from .terminal_configuration_create_body_tipping_obj0_nzd import (
    TerminalConfigurationCreateBodyTippingObj0Nzd,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Nzd,
)
from .terminal_configuration_create_body_tipping_obj0_pln import (
    TerminalConfigurationCreateBodyTippingObj0Pln,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Pln,
)
from .terminal_configuration_create_body_tipping_obj0_sek import (
    TerminalConfigurationCreateBodyTippingObj0Sek,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Sek,
)
from .terminal_configuration_create_body_tipping_obj0_sgd import (
    TerminalConfigurationCreateBodyTippingObj0Sgd,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Sgd,
)
from .terminal_configuration_create_body_tipping_obj0_usd import (
    TerminalConfigurationCreateBodyTippingObj0Usd,
    _SerializerTerminalConfigurationCreateBodyTippingObj0Usd,
)


class TerminalConfigurationCreateBodyTippingObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationCreateBodyTippingObj0
    """

    aud: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Aud]

    cad: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Cad]

    chf: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Chf]

    czk: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Czk]

    dkk: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Dkk]

    eur: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Eur]

    gbp: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Gbp]

    hkd: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Hkd]

    jpy: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Jpy]

    myr: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Myr]

    nok: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Nok]

    nzd: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Nzd]

    pln: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Pln]

    sek: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Sek]

    sgd: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Sgd]

    usd: typing_extensions.NotRequired[TerminalConfigurationCreateBodyTippingObj0Usd]


class _SerializerTerminalConfigurationCreateBodyTippingObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyTippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    aud: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Aud] = (
        pydantic.Field(alias="aud", default=None)
    )
    cad: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Cad] = (
        pydantic.Field(alias="cad", default=None)
    )
    chf: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Chf] = (
        pydantic.Field(alias="chf", default=None)
    )
    czk: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Czk] = (
        pydantic.Field(alias="czk", default=None)
    )
    dkk: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Dkk] = (
        pydantic.Field(alias="dkk", default=None)
    )
    eur: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Eur] = (
        pydantic.Field(alias="eur", default=None)
    )
    gbp: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Gbp] = (
        pydantic.Field(alias="gbp", default=None)
    )
    hkd: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Hkd] = (
        pydantic.Field(alias="hkd", default=None)
    )
    jpy: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Jpy] = (
        pydantic.Field(alias="jpy", default=None)
    )
    myr: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Myr] = (
        pydantic.Field(alias="myr", default=None)
    )
    nok: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Nok] = (
        pydantic.Field(alias="nok", default=None)
    )
    nzd: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Nzd] = (
        pydantic.Field(alias="nzd", default=None)
    )
    pln: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Pln] = (
        pydantic.Field(alias="pln", default=None)
    )
    sek: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Sek] = (
        pydantic.Field(alias="sek", default=None)
    )
    sgd: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Sgd] = (
        pydantic.Field(alias="sgd", default=None)
    )
    usd: typing.Optional[_SerializerTerminalConfigurationCreateBodyTippingObj0Usd] = (
        pydantic.Field(alias="usd", default=None)
    )
