import platform

from .AdapterInterface import AdapterInterface


class MacAdapter(AdapterInterface):
    @staticmethod
    def is_available():
        return platform.system() == 'Darwin'

    def __init__(self):
        print('{} loaded.'.format(self.__class__.__name__))
