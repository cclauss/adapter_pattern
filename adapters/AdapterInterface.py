import importlib
import inspect
import os


class AdapterInterface(object):
    @classmethod
    def is_available(cls):
        raise NotImplementedError()

    def __init__(self):
        print('Adapter {} loaded.'.format(self.__class__.__name__))

    def perform_action():
        raise NotImplementedError()


def _is_adapter(cls):
    return (inspect.isclass(cls) and issubclass(cls, AdapterInterface) and
            cls != AdapterInterface)


def _get_adapter_classes():
    dirname = os.path.dirname(os.path.abspath(__file__))
    adapter_classes = []
    for file_name in sorted(os.listdir(dirname)):
        root, ext = os.path.splitext(file_name)
        if ext.lower() == '.py':
            module = importlib.import_module('.' + root, 'adapters')
            for _, cls in inspect.getmembers(module, _is_adapter):
                adapter_classes.append(cls)
    return adapter_classes


def get_adapters():
    return {cls.__name__.lower(): cls for cls in _get_adapter_classes()}
