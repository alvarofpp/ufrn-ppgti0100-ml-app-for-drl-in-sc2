import streamlit as st
from app.views.components import SidebarComponent, MessageFeedbackComponent
from app.config import get_config


def main():
    sidebar = SidebarComponent(render_component=st)
    sidebar.render()
    page = sidebar.get_selected_page()

    message_feedback_component = MessageFeedbackComponent()
    if message_feedback_component.condition():
        message_feedback_component.render()

    with st.spinner(f'Carregando {page} ...'):
        page.render()


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )
    main()
