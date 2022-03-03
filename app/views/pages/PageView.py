import abc

from app.core.mixins import CheckMethodsMixin
import streamlit as st


class PageView(CheckMethodsMixin, abc.ABC):
    _methods = [
        'intro',
    ]

    def __init__(self):
        self.title = ''
        self._check_class()

    @abc.abstractmethod
    def intro(self):
        raise NotImplementedError('You must implement the "intro" method.')

    def render(self):
        st.title(self.title.upper())
        self.intro()
        self.horizontal_rule()
        for section in self.__get_sections():
            getattr(self, section)()

    def horizontal_rule(self):
        st.markdown('---')

    def __get_sections(self):
        return sorted([dir for dir in self.__dir__() if dir.startswith('section_')])
