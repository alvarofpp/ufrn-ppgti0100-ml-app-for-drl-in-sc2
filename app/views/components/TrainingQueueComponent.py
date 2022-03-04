from app import SessionState
from app.views.components import Component


class TrainingQueueComponent(Component):
    def render(self):
        queue = SessionState.get('queue')

        if len(queue) == 0:
            self.render_component.text('Nenhum treinamento na base.')
            return

        for queue_element in queue:
            self.render_component.code(queue_element)
