import platform

from .AdapterInterface import AdapterInterface


class WindowsAdapter(AdapterInterface):
    @classmethod
    def is_available(cls):
        return platform.system() == 'Windows'

    def __init__(self):
        print('{} loaded.'.format(self.__class__.__name__))
