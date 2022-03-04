import sys

from absl.flags import FLAGS
from app import SessionState
from app.core.queue import TrainingElement
from game.agents import PlayerToAgent
from game.bots import PlayerToBot
from game.envs import EnvBasic


class Game:
    def __init__(self, training_element: TrainingElement):
        SessionState.set('training_in_progress_data', training_element)
        self.training_element = training_element
        self.max_matches = training_element.config['max_matches']
        FLAGS(sys.argv)

    def _init_env(self):
        self.agents = []
        players_env = []
        for player in self.training_element.config['players']:
            if player['is_agent']:
                players_env.append(PlayerToAgent.convert(player))
                self.agents.append(PlayerToAgent.get_agent_by_name(player))
            else:
                players_env.append(PlayerToBot.convert(player))

        self.env = EnvBasic.init({
            'map_name': self.training_element.config['map'],
            'players': players_env,
        })

    def start(self):
        SessionState.set('training_in_progress', True)
        try:
            matches = 0
            while matches < self.max_matches:
                self._init_env()
                with self.env as env:
                    timesteps = env.reset()

                    while True:
                        step_actions = [agent.step(timesteps[0]) for agent in self.agents]
                        if timesteps[0].last():
                            matches += 1
                            self.training_element.matches_runned += 1
                            SessionState.set('training_in_progress_data', self.training_element)
                            break
                        timesteps = env.step(step_actions)
        except KeyboardInterrupt:
            pass

        SessionState.set('training_in_progress', False)
        SessionState.set('training_in_progress_data', None)
