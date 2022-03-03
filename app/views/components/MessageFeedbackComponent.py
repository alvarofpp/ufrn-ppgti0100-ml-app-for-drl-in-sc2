from app import SessionState
from app.views.components import Component


class MessageFeedbackComponent(Component):
    def condition(self) -> bool:
        return SessionState.get('message_feedback') is not None

    def render(self):
        message_feedback = SessionState.get('message_feedback')

        if message_feedback['type'] == 'info':
            self._render_info(message_feedback['message'])

        SessionState.clear('message_feedback')

    def _render_info(self, message: str):
        self.render_component.info(message)
