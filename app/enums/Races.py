from enum import Enum

from app.core.mixins import EnumToListMixin
from pysc2.env.sc2_env import Race


class Races(EnumToListMixin, Enum):
    RANDOM = 'Random'
    PROTOSS = 'Protoss'
    TERRAN = 'Terran'
    ZERG = 'Zerg'

    @staticmethod
    def convert_to_sc2(value: str) -> Race:
        map_values = {
            Races.RANDOM: Race.random,
            Races.PROTOSS: Race.protoss,
            Races.TERRAN: Race.terran,
            Races.ZERG: Race.zerg,
        }

        if value not in map_values.keys():
            return Race.random

        return map_values[value]
