from typing import Dict

from pysc2.env.sc2_env import SC2Env
from pysc2.lib import features


class EnvBasic:
    @staticmethod
    def init(env_data: Dict) -> SC2Env:
        configs = {
            'agent_interface_format': features.AgentInterfaceFormat(
                feature_dimensions=features.Dimensions(screen=84, minimap=64),
                use_feature_units=True,
            ),
            'step_mul': 16,
            'game_steps_per_episode': 0,
            'visualize': True,
        }

        return SC2Env(**configs, **env_data)
