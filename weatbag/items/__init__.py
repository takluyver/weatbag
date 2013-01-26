from importlib import import_module
from types import ModuleType

def get_item_module(name):
    """Returns the module for that item, or a blank module if no module exists.
    """
    name = name.replace(' ','_')
    try:
        return import_module('weatbag.items.' + name)
    except ImportError:
        return ModuleType(name, "Dummy Module")


def _combine(item1, item2):
    "Try combining items one way"
    try:
        return get_item_module(item1).combine(item2)
    except AttributeError:
        pass

def combine(item1, item2):
    "Try combining items either way round."
    results = _combine(item1, item2)
    if results is None:
        results = _combine(item2, item1)
    return results
