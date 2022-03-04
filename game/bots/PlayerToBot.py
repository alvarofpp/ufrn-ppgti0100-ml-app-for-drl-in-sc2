from typing import Dict

from app.enums import Difficulties, Races
from pysc2.env.sc2_env import Bot


class PlayerToBot:
    @staticmethod
    def convert(player_data: Dict) -> Bot:
        race = Races.convert_to_sc2(player_data['race'])
        difficulty = Difficulties.convert_to_sc2(player_data['difficulty'])
        return Bot(race, difficulty)
