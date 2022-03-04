import sys

from absl.flags import FLAGS
from app.core.queue import TrainingElement
from game.agents import PlayerToAgent
from game.bots import PlayerToBot
from game.envs import EnvBasic


class Game:
    def __init__(self, training_element: TrainingElement):
        self.max_matches = training_element.config['max_matches']
        FLAGS(sys.argv)

        self.agents = []
        players_env = []
        for player in training_element.config['players']:
            if player['is_agent']:
                players_env.append(PlayerToAgent.convert(player))
                self.agents.append(PlayerToAgent.get_agent_by_name(player))
            else:
                players_env.append(PlayerToBot.convert(player))

        self.env = EnvBasic.init({
            'map_name': training_element.config['map'],
            'players': players_env,
        })

    def start(self):
        try:
            matches = 0
            while matches < self.max_matches:
                with self.env as env:
                    timesteps = env.reset()

                    while True:
                        step_actions = [agent.step(timesteps[0]) for agent in self.agents]
                        if timesteps[0].last():
                            matches += 1
                            break
                        timesteps = env.step(step_actions)
        except KeyboardInterrupt:
            pass
