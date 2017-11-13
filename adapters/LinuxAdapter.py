import platform

from .AdapterInterface import AdapterInterface


class LinuxAdapter(AdapterInterface):
    @staticmethod
    def is_available():
        return platform.system() == 'Linux'

    def __init__(self):
        print('{} loaded.'.format(self.__class__.__name__))
