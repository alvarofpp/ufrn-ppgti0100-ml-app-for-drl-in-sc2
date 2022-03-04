from app.views import pages
from app.views.components import Component, TrainingQueueComponent


class SidebarComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(render_component=kwargs['render_component'].sidebar)
        self.data = {
            'page': None,
        }

    # @st.cache(allow_output_mutation=True)
    def get_page(self):
        training_index_page = pages.TrainingIndexPage()
        training_create_page = pages.TrainingCreatePage()

        return {
            training_index_page.title: training_index_page,
            training_create_page.title: training_create_page,
        }

    def render(self):
        self.render_component.title('Menu de Navegação')
        self.data['page'] = self.render_component.radio(
            'Ir para',
            list(self.get_page().keys()),
        )
        self.render_component.markdown("""
        ---
        Base de treinamentos:
        """)
        component = TrainingQueueComponent.TrainingQueueComponent(
            render_component=self.render_component,
        )
        component.render()

    def get_selected_page(self):
        return self.get_page()[self.data['page']]
