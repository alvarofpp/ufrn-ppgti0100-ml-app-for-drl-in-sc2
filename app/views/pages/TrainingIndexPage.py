from app import SessionState
from app.views.components import TrainingElementComponent
from app.views.pages import PageView
from game import Game
import streamlit as st


class TrainingIndexPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Treinamentos'
        self.all_trainings = False

    def intro(self):
        st.markdown("""
        Nessa página você conseguirá acompanhar os seus treinamentos.
        """, unsafe_allow_html=True)

    def section_01(self):
        st.markdown("""
        ## Base de treinamentos
        """, unsafe_allow_html=True)
        queue = SessionState.get('queue')
        len_queue = len(queue)

        if len_queue == 0:
            st.warning('Não há treinamentos na base.')
            return

        st.text('Há um total de {} treinamento{} na base.'.format(
            len_queue,
            's' if len_queue > 1 else '',
        ))

        queue.sort(key=lambda element: element.priority, reverse=True)

        self.all_trainings = False
        if st.button(
                '▶ Executar todos os treinamentos',
                help='Executar treinamento',
        ):
            self.all_trainings = True

        for element in queue:
            TrainingElementComponent.TrainingElementComponent().render(element)

        if self.all_trainings:
            for element in queue:
                Game(element).start()
