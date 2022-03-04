from app.enums import Difficulties, Races
from app.views.components import Component
from game.agents import AGENTS


class PlayerComponent(Component):
    def __init__(self, player_number: int = None, **kwargs):
        super().__init__(**kwargs)
        self.player_number = player_number
        self.data = {
            'race': None,
        }

    def render(self):
        self.render_component.markdown('**Player {}**'.format(self.player_number + 1))
        self.data['is_agent'] = self.render_component.checkbox(
            'Agente',
            key='checkbox_agent_p{}'.format(self.player_number),
        )
        self.data['race'] = self.render_component.selectbox(
            'Raça',
            Races.list(),
            key='select_race_p{}'.format(self.player_number),
        )

        if self.data['is_agent']:
            return self._render_player()

        return self._render_bot()

    def _render_player(self):
        self.data['agent'] = self.render_component.selectbox(
            'Agente',
            AGENTS,
            key='select_agent_p{}'.format(self.player_number),
        )
        pass

    def _render_bot(self):
        self.data['difficulty'] = self.render_component.selectbox(
            'Dificuldade',
            Difficulties.list(),
            key='select_difficulty_p{}'.format(self.player_number),
        )
