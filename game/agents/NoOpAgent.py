from pysc2.agents import base_agent
from pysc2.lib import actions


class NoOpAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(NoOpAgent, self).step(obs)

        return actions.RAW_FUNCTIONS.no_op()
