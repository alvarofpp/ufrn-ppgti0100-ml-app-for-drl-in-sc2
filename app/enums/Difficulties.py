from enum import Enum

from app.core.mixins import EnumToListMixin
from pysc2.env.sc2_env import Difficulty


class Difficulties(EnumToListMixin, Enum):
    VERY_EASY = 'VeryEasy'
    EASY = 'Easy'
    MEDIUM = 'Medium'
    MEDIUM_HARD = 'MediumHard'
    HARD = 'Hard'
    HARDER = 'Harder'
    VERY_HARD = 'VeryHard'
    CHEAT_VISION = 'CheatVision'
    CHEAT_MONEY = 'CheatMoney'
    CHEAT_INSANE = 'CheatInsane'

    @staticmethod
    def convert_to_sc2(value: str) -> Difficulty:
        map_values = {
            Difficulties.VERY_EASY: Difficulty.very_easy,
            Difficulties.EASY: Difficulty.easy,
            Difficulties.MEDIUM: Difficulty.medium,
            Difficulties.MEDIUM_HARD: Difficulty.medium_hard,
            Difficulties.HARD: Difficulty.hard,
            Difficulties.HARDER: Difficulty.harder,
            Difficulties.VERY_HARD: Difficulty.very_hard,
            Difficulties.CHEAT_VISION: Difficulty.cheat_vision,
            Difficulties.CHEAT_MONEY: Difficulty.cheat_money,
            Difficulties.CHEAT_INSANE: Difficulty.cheat_insane,
        }

        if value not in map_values.keys():
            return Difficulty.easy

        return map_values[value]
