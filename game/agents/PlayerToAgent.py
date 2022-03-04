from typing import Dict

from app.enums import Races
import game.agents as agents
from pysc2.env.sc2_env import Agent


class PlayerToAgent:
    @staticmethod
    def convert(player_data: Dict) -> Agent:
        race = Races.convert_to_sc2(player_data['race'])
        return Agent(race)

    @staticmethod
    def get_agent_by_name(agent_name: str):
        if agent_name == 'RandomAgent':
            return agents.RandomAgent()
        if agent_name == 'SmartAgent':
            return agents.SmartAgent()

        return agents.NoOpAgent()
