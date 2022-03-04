import random

from game.agents.base import BaseAgent


class RandomAgent(BaseAgent):
    def step(self, obs):
        super(RandomAgent, self).step(obs)
        action = random.choice(self.actions)
        return getattr(self, action)(obs)
