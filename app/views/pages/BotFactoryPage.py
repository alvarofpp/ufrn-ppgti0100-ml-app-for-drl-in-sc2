from app.views.pages import PageView
import streamlit as st


class BotFactoryPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Fábrica de bots'

    def intro(self):
        st.markdown("""
        Nessa página você conseguirá selecionar as partes necessárias para gerar um bot novo.
        """, unsafe_allow_html=True)

    def section_01(self):
        st.markdown("""
        ## Docente
        """, unsafe_allow_html=True)
