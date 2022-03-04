from app import SessionState
from app.core.queue import TrainingElement, TrainingQueue
from app.views.components import Component
from game import Game


class QueueElementComponent(Component):
    def render(self, training_element: TrainingElement):
        self.render_component.markdown('### {}'.format(training_element.name))
        column_one, column_two = self.render_component.columns([1, 1])

        if column_one.button(
                '▶ Executar treinamento',
                help='Executar treinamento',
                key='btn_exec_{}'.format(training_element.id),
        ):
            # TODO
            Game(training_element).start()
            TrainingQueue.remove_training_from_queue(training_element.id)
            SessionState.set('message_feedback', {
                'type': 'info',
                'message': 'Treinamento iniciado.',
            })
        if column_two.button(
                '🗑 Remover treinamento',
                help='Remover treinamento da fila',
                key='btn_remove_{}'.format(training_element.id),
        ):
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
            training_element.created_at.strftime('%d/%m/%Y %H:%M:%S'),
        ))
        self.render_component.json(training_element.config)
