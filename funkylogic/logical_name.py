"""
Organizes name-generation functions for LogicalExpressions.

These functions depend on LogicalExpression being Iterable and Sized

@todo: This can be grouped with something else - into a larger module.
"""

def length_dispatch(logical):
    """
    @type: logical: LogicalExpression
    @rtype: Callable
    """
    if len(logical) == 0:
        return nullary
    elif len(logical) == 1:
        return unary
    elif len(logical) == 2:
        return binary
    else:
        return n_ary

def nullary(logical):
    """
    @type: logical: LogicalExpression
    @rtype: str
    """
    return type(logical).__name__

def unary(logical):
    """
    @type: logical: LogicalExpression
    @rtype: str
    """
    return "{name} {value}".format(
        name=type(logical).__name__,
        value=iter(logical).next()
    )

def binary(logical):
    """
    @type: logical: LogicalExpression
    @rtype: str
    """
    iterator = iter(logical)
    return "({left} {name} {right}".format(
        left=iterator.next(),
        name=type(logical).__name__,
        right=iterator.next()
    )

def n_ary(logical):
    """
    @type: logical: LogicalExpression
    @rtype: str
    """
    return "{name}({terms})".format(
        name=type(logical).__name__,
        terms=", ".join(logical)
    )
