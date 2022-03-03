from app import SessionState
from app.views.components import Component  # , QueueElementComponent


class TrainingQueueComponent(Component):
    def render(self):
        queue = SessionState.get('queue')

        if len(queue) == 0:
            self.render_component.text('Nenhum treinamento em andamento.')
            return

        # for queue_element in queue:
        #     QueueElementComponent(render_component=self.render_component).render(queue_element)
