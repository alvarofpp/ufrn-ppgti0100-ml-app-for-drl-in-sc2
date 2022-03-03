from uuid import UUID
from app import SessionState
from app.config import get_config
from app.core.queue import TrainingElement


class TrainingQueue:
    @staticmethod
    def add_training_to_queue(training_data: TrainingElement):
        queue = SessionState.get('queue')

        if len(queue) >= get_config('queue.maxsize'):
            return

        index_to_split = 0
        for index in range(0, len(queue)):
            if queue[index].priority < training_data.priority:
                index_to_split = index
                break

        new_queue = queue[:index_to_split] + [training_data] + queue[index_to_split:]
        SessionState.set('queue', new_queue)

    @staticmethod
    def remove_training_from_queue(id: UUID):
        queue = SessionState.get('queue')

        for index in range(0, len(queue)):
            element = queue[index]
            if element.id == id:
                new_queue = queue[:index] + queue[index+1:]
                SessionState.set('queue', new_queue)
                del element
                break
