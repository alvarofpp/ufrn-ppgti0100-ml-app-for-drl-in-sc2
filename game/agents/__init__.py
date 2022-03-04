from .NoOpAgent import NoOpAgent
from .PlayerToAgent import PlayerToAgent
from .RandomAgent import RandomAgent
from .SmartAgent import SmartAgent

AGENTS = [
    'NoOpAgent',
    'RandomAgent',
    'SmartAgent',
]

__all__ = [
    'AGENTS',
    'NoOpAgent',
    'PlayerToAgent',
    'RandomAgent',
    'SmartAgent',
]
