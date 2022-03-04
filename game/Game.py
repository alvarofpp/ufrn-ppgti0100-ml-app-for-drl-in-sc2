import sys
from absl.flags import FLAGS

from app.core.queue import TrainingElement
from game.agents import PlayerToAgent, RawAgent
from game.bots import PlayerToBot
from game.envs import EnvBasic


class Game:
    def __init__(self, training_element: TrainingElement):
        self.max_matches = training_element.config['max_matches']
        FLAGS(sys.argv)
        self.env = EnvBasic.init({
            'map_name': training_element.config['map'],
            'players': [
                PlayerToAgent.convert(player)
                if player['is_agent'] else PlayerToBot.convert(player)
                for player in training_element.config['players']
            ],
        })

    def start(self):
        agent = RawAgent()
        try:
            matches = 0
            while matches < self.max_matches:
                with self.env as env:
                    timesteps = env.reset()

                    while True:
                        step_actions = [agent.step(timesteps[0])]
                        if timesteps[0].last():
                            matches += 1
                            break
                        timesteps = env.step(step_actions)
        except KeyboardInterrupt:
            pass
