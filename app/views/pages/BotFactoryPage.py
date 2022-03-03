import streamlit as st

from app.views.pages import PageView


class BotFactoryPage(PageView):

    def __init__(self):
        super().__init__()
        self.title = 'Fábrica de bots'

    def intro(self):
        st.markdown('''
        Nessa página você conseguirá selecionar as partes necessárias para gerar um bot novo.
        ''', unsafe_allow_html=True)

    def section_01(self):
        st.markdown('''
        ## Docente

        Aqui você poderá buscar por um docente e visualizar a sua taxa de aprovação para cada disciplina lecionada por ele.
        ''', unsafe_allow_html=True)
        # option_docente = st.selectbox('Docente',
        #                               options=self.data['siape'].unique().tolist(),
        #                               format_func=self.format_func_docentes),

