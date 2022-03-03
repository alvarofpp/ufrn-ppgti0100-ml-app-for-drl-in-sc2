from app.views.components import Component, TrainingQueueComponent
from app.views import pages
from app import SessionState


class SidebarComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(render_component=kwargs['render_component'].sidebar)
        self.data = {
            'page': None,
        }

    # @st.cache(allow_output_mutation=True)
    def get_page(self):
        bot_factory_page = pages.BotFactoryPage()
        queue_page = pages.QueuePage()
        training_page = pages.TrainingPage()

        return {
            bot_factory_page.title: bot_factory_page,
            queue_page.title: queue_page,
            training_page.title: training_page,
        }

    def render(self):
        self.render_component.title('Menu de Navegação')
        self.data['page'] = self.render_component.radio(
            'Ir para',
            list(self.get_page().keys()),
        )
        self.render_component.markdown("""
        ---
        Fila de treinamentos:
        """)
        component = TrainingQueueComponent.TrainingQueueComponent(
            render_component=self.render_component,
        )
        component.render()

    def get_selected_page(self):
        return self.get_page()[self.data['page']]
