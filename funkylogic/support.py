"""
Basic convenience and internal-support functions.

Treatment of IS_NONSTRING_ITERABLE is not Python 3 compatible (basestring)
"""
import functools
import collections

NOT_IMPLEMENTED = lambda self, *args, **kwargs: NotImplemented

IS_NONSTRING_ITERABLE = lambda obj: (
    isinstance(obj, collections.Iterable)
    and not isinstance(obj, basestring)
)

def to_set(value):
    """
    @type: value: Any
    @rtype: set
    """
    if isinstance(value, set):
        return value
    elif IS_NONSTRING_ITERABLE(value):
        return set(value)
    else:
        return set([value])


def Union(*terms):  # pylint: disable=invalid-name
    """
    @type: terms: Sequence[Any]
    @rtype: set[Any]
    """
    accumulator = set()
    for term in terms:
        accumulator = accumulator.union(to_set(term))
    return accumulator

def Intersection(*terms):  # pylint: disable=invalid-name
    """
    @type: terms: Sequence[Any]
    @rtype: set[Any]
    """
    accumulator = set()
    for term in terms:
        accumulator = accumulator.intersection(to_set(term))
    return accumulator

def Difference(left, right):  # pylint: disable=invalid-name
    """
    @type: left: Iterable[Any]
    @rtype: set[Any]
    """
    return to_set(left).difference(to_set(right))



