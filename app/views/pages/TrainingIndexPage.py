from app import SessionState
from app.views.components import TrainingElementComponent
from app.views.pages import PageView
import streamlit as st


class TrainingIndexPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Treinamentos'

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

        for element in queue:
            TrainingElementComponent.TrainingElementComponent().render(element)
