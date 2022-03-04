import json

from app import SessionState
from app.constants import LADDER_MAPS, PRIORITIES
from app.core.queue import TrainingElement, TrainingQueue
from app.views.components import PlayerComponent, SelectComponent
from app.views.pages import PageView
import streamlit as st


class TrainingPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Treinamentos'
        self.data = {
            'map': None,
            'number_players': 2,
            'players': [],
        }

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
            }

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
        )
        self.data['description'] = st.text_area(
            'Descrição',
            height=100,
            max_chars=5000,
        )
        self.data['max_matches'] = st.slider(
            'Quantidade de máxima de partidas',
            min_value=1,
            max_value=10000,
            step=50,
        )

        st.markdown("""
        ## Mapa
        """, unsafe_allow_html=True)
        self.data['map'] = st.selectbox('Mapa', LADDER_MAPS)

        st.markdown("""
        ## Players
        """, unsafe_allow_html=True)
        self.data['number_players'] = st.slider('Quantidade de players', min_value=2, max_value=8)
        column_one, column_two = st.columns(2)

        for player_number in range(0, self.data['number_players']):
            column = column_one if (player_number - 1) % 2 != 0 else column_two
            player_component = PlayerComponent(player_number=player_number, render_component=column)
            player_component.render()
            self.data['players'].append(player_component.data)

        if st.button('Adicionar treinamento a fila'):
            training_data = TrainingElement.create_training_element(self.data)
            TrainingQueue.add_training_to_queue(training_data)
            SessionState.set('message_feedback', {
                'type': 'info',
                'message': 'Treinamento adicionado a fila com sucesso',
            })

        st.json(self.data)
