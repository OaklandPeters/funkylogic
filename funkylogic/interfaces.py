"""
Interfaces and generic functions related to LogicalExpression
"""
import abc
import collections

from .extern import ducktype

from . import support

class LogicalInterface(collections.Sequence):
    operation = abc.abstractmethod(support.NOT_IMPLEMENTED)
    map = abc.abstractmethod(support.NOT_IMPLEMENTED)
    call = abc.abstractmethod(support.NOT_IMPLEMENTED)
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is LogicalInterface:
            if ducktype.meets(subclass, LogicalInterface):
                return True
        return NotImplemented


_IS_LOGICAL = lambda obj: isinstance(obj, LogicalInterface)


def _map(term, predicate):
    """
    A 'generic-function' verison of map, which defers
    to term.map, if one exists, and otherwise calls predicate
    on term.
    Actually iterable mapping is handled by term.map
    """
    # validate(predicate, collections.Callable)
    if _IS_LOGICAL(term):
        return term.map(predicate)
    else:
        return predicate(term)

def _call(term):
    """
    A 'generic-function' version of call
    """
    if _IS_LOGICAL(term):
        return term.call()
    else:
        return term

