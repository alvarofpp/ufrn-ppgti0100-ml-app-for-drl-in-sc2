from typing import Dict

from app.enums import Races
from pysc2.env.sc2_env import Agent


class PlayerToAgent:
    @staticmethod
    def convert(player_data: Dict) -> Agent:
        race = Races.convert_to_sc2(player_data['race'])
        return Agent(race)
