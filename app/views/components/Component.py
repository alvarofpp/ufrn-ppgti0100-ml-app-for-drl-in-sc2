import abc

from app.core.mixins import CheckMethodsMixin, RenderMixin


class Component(RenderMixin, CheckMethodsMixin, abc.ABC):
    _methods = [
        'render',
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._check_class()
