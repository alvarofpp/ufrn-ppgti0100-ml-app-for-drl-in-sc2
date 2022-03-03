from typing import Dict

from app.views.components import Component
from app.constants import RACES, DIFFICULTY


class PlayerComponent(Component):
    def __init__(self, player_number: int = None, **kwargs):
        super().__init__(**kwargs)
        self.player_number = player_number
        self.data = {
            'race': None,
        }

    def render(self):
        self.render_component.markdown('**Player {}**'.format(self.player_number + 1))
        self.data['race'] = self.render_component.selectbox(
            'Raça',
            RACES,
            key='select_race_p{}'.format(self.player_number)
        )

        if self.data['race'] == 'Player':
            return self._render_player()

        return self._render_bot()

    def _render_player(self):
        pass

    def _render_bot(self):
        self.data['difficulty'] = self.render_component.selectbox(
            'Dificuldade',
            DIFFICULTY,
            key='select_race_p{}'.format(self.player_number)
        )
