from dataclasses import dataclass, field
from typing import Dict
import uuid
from datetime import datetime


@dataclass(order=True)
class TrainingElement:
    priority: int
    id: uuid.UUID = field(compare=False)
    name: str = field(compare=False)
    description: str = field(compare=False)
    created_at: datetime = field(compare=False)
    config: Dict = field(compare=False)
    matches_runned: int = field(compare=False)

    @staticmethod
    def create_training_element(training_data: Dict):
        return TrainingElement(
            priority=training_data['priority'],
            id=uuid.uuid4(),
            name=training_data['name'] if training_data['name'] else uuid.uuid4(),
            description=training_data['description'],
            created_at=datetime.now(),
            config={
                'players': training_data['players'],
                'map': training_data['map'],
                'max_matches': training_data['max_matches'],
            },
            matches_runned=0,
        )
