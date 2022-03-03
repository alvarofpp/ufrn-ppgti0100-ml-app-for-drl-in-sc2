import streamlit as st

from app import SessionState
from app.views.pages import PageView
from app.views.components import QueueElementComponent


class QueuePage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Fila de treinamentos'

    def intro(self):
        st.markdown('''
        Nessa página você conseguirá acompanhar os seus treinamentos.
        ''', unsafe_allow_html=True)

    def section_01(self):
        st.markdown('''
        ## Fila
        ''', unsafe_allow_html=True)
        queue = SessionState.get('queue')
        len_queue = len(queue)

        if len_queue == 0:
            st.warning('Não há treinamentos na fila.')
            return

        st.text('Há um total de {} treinamento{} na fila.'.format(
            len_queue,
            's' if len_queue > 1 else ''
        ))

        for element in queue:
            QueueElementComponent().render(element)
