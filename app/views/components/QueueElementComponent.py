from app import SessionState
from app.core.queue import TrainingElement, TrainingQueue
from app.views.components import Component


class QueueElementComponent(Component):
    def render(self, training_element: TrainingElement):
        self.render_component.markdown('### {}'.format(training_element.name))
        column_one, column_two = self.render_component.columns([1, 1])

        if column_one.button('▶ Executar treinamento', help='Executar treinamento'):
            TrainingQueue.remove_training_from_queue(training_element.id)
            SessionState.set('message_feedback', {
                'type': 'info',
                'message': 'Treinamento excluído com sucesso',
            })
        if column_two.button('🗑 Remover treinamento', help='Remover treinamento da fila'):
            TrainingQueue.remove_training_from_queue(training_element.id)
            SessionState.set('message_feedback', {
                'type': 'info',
                'message': 'Treinamento excluído com sucesso',
            })

        if training_element.description:
            self.render_component.markdown(training_element.description)

        self.render_component.markdown("""
        - **ID**: {}
        - **Prioridade**: {}
        - **Data e hora de criação**: {}
        **Configurações**:
        """.format(
            training_element.id,
            training_element.priority,
            training_element.created_at.strftime("%d/%m/%Y %H:%M:%S")
        ))
        self.render_component.json(training_element.config)
