from typing import Dict

from app.enums import Difficulties, Races
from app.views.components import Component
from game.agents import AGENTS


class PlayerComponent(Component):
    def __init__(self, player_number: int = None, player_data: Dict = None, **kwargs):
        super().__init__(**kwargs)
        self.player_number = player_number
        self.data = {
            'is_agent': False,
            'race': None,
        }

        if player_data is not None:
            self.data = {
                'is_agent': player_data['is_agent'],
                'race': player_data['race'],
            }
            if player_data['is_agent']:
                self.data['agent'] = player_data['agent']
            else:
                self.data['difficulty'] = player_data['difficulty']

    def render(self):
        self.render_component.markdown('**Player {}**'.format(self.player_number + 1))
        self.data['is_agent'] = self.render_component.checkbox(
            'Agente',
            key='checkbox_agent_p{}'.format(self.player_number),
            value=self.data['is_agent'],
        )

        race_index = 0
        if self.data['race'] is not None:
            race_index = Races.list().index(self.data['race'])

        self.data['race'] = self.render_component.selectbox(
            'Raça',
            Races.list(),
            key='select_race_p{}'.format(self.player_number),
            index=race_index,
        )

        if self.data['is_agent']:
            return self._render_player()

        return self._render_bot()

    def _render_player(self):
        agent_index = 0

        if 'agent' in self.data.keys() and self.data['agent'] is not None:
            agent_index = AGENTS.index(self.data['agent'])

        self.data['agent'] = self.render_component.selectbox(
            'Agente',
            AGENTS,
            key='select_agent_p{}'.format(self.player_number),
            index=agent_index,
        )

    def _render_bot(self):
        difficulty_index = 0

        if 'difficulty' in self.data.keys() and self.data['difficulty'] is not None:
            difficulty_index = Difficulties.list().index(self.data['difficulty'])

        self.data['difficulty'] = self.render_component.selectbox(
            'Dificuldade',
            Difficulties.list(),
            key='select_difficulty_p{}'.format(self.player_number),
            index=difficulty_index,
        )
