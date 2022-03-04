import json

from app import SessionState
from app.constants import PRIORITIES
from app.core.queue import TrainingElement, TrainingQueue
from app.views.components import PlayerComponent, SelectComponent
from app.views.pages import PageView
from pysc2.env.sc2_env import maps
import streamlit as st


class TrainingCreatePage(PageView):
    def __init__(self):
        super().__init__()
        self.title = 'Registrar treinamento'
        self.data = SessionState.get('training_create_data')
        self.maps = maps.get_maps()

    def _reset_data(self):
        self.data = {
            'priority': 1,
            'name': '',
            'description': '',
            'map': None,
            'number_players': 2,
            'players': [],
            'max_matches': 1,
        }

        SessionState.set('training_create_data', self.data)

    def intro(self):
        st.markdown("""
        Aqui é onde você parametriza seus treinamentos e acompanha o seu desenvolvimento.
        """, unsafe_allow_html=True)

        config_file = st.file_uploader('Importar configurações')
        if config_file is not None:
            data = json.loads(config_file.getvalue())
            self.data = {
                'priority': data['priority'],
                'name': data['name'],
                'description': data['description'],
                'map': data['config']['map'],
                'number_players': len(data['config']['players']),
                'players': data['config']['players'],
                'max_matches': data['config']['max_matches'],
            }
            SessionState.set('training_create_data', self.data)

        if self.data is None:
            self._reset_data()

        if st.button('Limpar formulário'):
            self._reset_data()

    def section_01(self):
        st.markdown("""
        ## Dados básicos
        """, unsafe_allow_html=True)

        self.data['priority'] = SelectComponent(
            render_component=st,
            values=PRIORITIES,
        ).render('Prioridade')
        self.data['name'] = st.text_input(
            'Nome',
            max_chars=250,
            value=self.data['name'],
        )
        self.data['description'] = st.text_area(
            'Descrição',
            height=100,
            max_chars=5000,
            value=self.data['description'],
        )
        self.data['max_matches'] = st.slider(
            'Quantidade de máxima de partidas',
            min_value=1,
            max_value=10000,
            step=50,
            value=self.data['max_matches'],
        )

        st.markdown("""
        ## Mapa
        """, unsafe_allow_html=True)
        map_index = 0
        if self.data['map'] is not None:
            map_index = list(self.maps.keys()).index(self.data['map'])

        self.data['map'] = st.selectbox(
            'Mapa',
            self.maps.keys(),
            index=map_index,
        )

        st.markdown("""
        ## Players
        """, unsafe_allow_html=True)

        max_players = self.maps[self.data['map']].players

        if max_players > 1:
            self.data['number_players'] = st.slider(
                'Quantidade de players',
                min_value=1,
                max_value=max_players,
                value=self.data['number_players'],
            )
        else:
            self.data['number_players'] = 1

        column_one, column_two = st.columns(2)
        self.data['players'] = []

        for player_number in range(0, self.data['number_players']):
            player_data = None
            if player_number < len(self.data['players']):
                player_data = self.data['players'][player_number]

            column = column_one if (player_number - 1) % 2 != 0 else column_two
            player_component = PlayerComponent(
                player_number=player_number,
                render_component=column,
                player_data=player_data,
            )
            player_component.render()
            self.data['players'].append(player_component.data)

        if st.button('Adicionar treinamento a base'):
            if not self._check_least_one_agent():
                st.warning('Ao menos 1 player deve ser um agente.')
                return

            training_data = TrainingElement.create_training_element(self.data)
            TrainingQueue.add_training_to_queue(training_data)
            SessionState.set('message_feedback', {
                'type': 'info',
                'message': 'Treinamento adicionado a fila com sucesso',
            })

        st.json(self.data)

    def _check_least_one_agent(self) -> bool:
        for player in self.data['players']:
            if player['is_agent']:
                return True

        return False
