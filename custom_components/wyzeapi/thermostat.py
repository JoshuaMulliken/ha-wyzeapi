"""Platform for thermostat integration."""
import asyncio
import logging
from typing import Optional, List
from enum import Enum

from homeassistant.components.climate import ClimateEntity
from homeassistant.const import ATTR_ATTRIBUTION

from . import DOMAIN
from wyzeapy.client import WyzeApiClient
# TODO add thermostat to devices
# from wyzeapy.devices import Switch

_LOGGER = logging.getLogger(__name__)
ATTRIBUTION = "Data provided by Wyze"


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Wyze Switch platform."""
    _LOGGER.debug("""Creating new WyzeApi switch component""")

    _ = config
    _ = discovery_info

    wyzeapi_client: WyzeApiClient = hass.data[DOMAIN]["wyzeapi_account"]

    # Add devices
    # TODO change to thermostat
    # switches = await wyzeapi_client.list_switches()
    # async_add_entities([HAWyzeSwitch(wyzeapi_client, switch) for switch in switches], True)


class HAWyzeSwitch(ClimateEntity):
    """Representation of a Wyze Switch."""

    __client: WyzeApiClient

    class State(Enum):
        HOME = 1
        AWAY = 2
        SLEEP = 3

    class Mode(Enum):
        OFF = 0
        HEAT = 1
        COOL = 2
        AUTO = 3


    def __init__(self, client: WyzeApiClient, thermostat):
        self.__client = client
        self.__thermostat = thermostat  # TODO add thermostat to the wyzeapy package

    @property
    def hvac_mode(self) -> str:
        pass

    @property
    def hvac_modes(self) -> List[str]:
        pass

    @property
    def target_temperature_high(self) -> Optional[float]:
        pass

    @property
    def target_temperature_low(self) -> Optional[float]:
        pass

    @property
    def preset_mode(self) -> Optional[str]:
        pass

    @property
    def preset_modes(self) -> Optional[List[str]]:
        pass

    @property
    def is_aux_heat(self) -> Optional[bool]:
        pass

    @property
    def fan_mode(self) -> Optional[str]:
        pass

    @property
    def fan_modes(self) -> Optional[List[str]]:
        pass

    @property
    def swing_mode(self) -> Optional[str]:
        pass

    @property
    def swing_modes(self) -> Optional[List[str]]:
        pass

    def set_temperature(self, **kwargs) -> None:
        pass

    def set_humidity(self, humidity: int) -> None:
        pass

    def set_fan_mode(self, fan_mode: str) -> None:
        pass

    def set_hvac_mode(self, hvac_mode: str) -> None:
        pass

    def set_swing_mode(self, swing_mode: str) -> None:
        pass

    def set_preset_mode(self, preset_mode: str) -> None:
        pass

    def turn_aux_heat_on(self) -> None:
        pass

    def turn_aux_heat_off(self) -> None:
        pass

    @property
    def supported_features(self) -> int:
        pass

    @property
    def temperature_unit(self) -> str:
        pass
