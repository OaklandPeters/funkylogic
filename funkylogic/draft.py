"""
Draft of the core class objects in funky-logic.

@todo: This is going to have to do some sort of dispatching on Intersection/Union
    ... defer to set.union for atomics, but use your own for LogicalUnion
@todo: Give LogicalExpression abstracts for Sequence
@todo: Incorporate type_check
"""
import collections
import abc
import functools

from funkylogic import interfaces
from funkylogic import support
from funkylogic import logical_name


class ConcreteSequence(collections.Sequence):
    def __init__(self, *terms):
        self.terms = terms
    def __iter__(self):
        return iter(self.terms)
    def __len__(self):
        return len(self.terms)
    def __contains__(self, other):
        return other in self.terms
    def __getitem__(self, key):
        return self.terms[key]
    #
    def __eq__(self, other):


        print()
        print("self.terms:", type(self.terms), self.terms)
        print()
        import pdb
        pdb.set_trace()
        print()
        
        if isinstance(other, interfaces.LogicalInterface):
            return self.terms == other.terms
        else:
            return self.terms == other




class Logical(interfaces.LogicalInterface):
    """
    This might become a parent object for LogicalExpression.
    ... or LogicalExpression might be renamed Logical

    NEW IDEA:
    This is the collection of class methods, and LogicalExpression
    handles nothing but __init__, and dispatching

    class Logical(LogicalInterface):
        @classmethod
        def map(cls, predicate, *terms):
            _terms = (interfaces._map(term, predicate) for term in terms)
            return cls(*_terms)
        @classmethod
        def call(cls, operation, *terms):
            _terms = (interfaces._call(term) for term in terms)
            return operation(*terms)


    class LogicalExpression(Logical, ConcreteSequence):
        def map(self, predicate):
            return Logical.map(predicate, self)
        def call(self):
            return Logical.call(self.operation, self)
        def collapse(self, predicate=bool):
            return self.map(predicate).call()


    class ConcreteSequence(collections.Sequence):
        def __init__(self, *terms):
            self.terms = terms
        def __iter__(self):
            return iter(self.terms)
        def __len__(self):
            return len(self.terms)
        def __contains__(self, other):
            return other in self.terms
        def __getitem__(self, key):
            return self.terms[key]


    """
    @classmethod
    def map(cls, predicate, *terms):
        _terms = (interfaces._map(term, predicate) for term in terms)
        return cls(*_terms)
    @classmethod
    def call(cls, operation, *terms):
        _terms = (interfaces._call(term) for term in terms)
        return operation(*terms)
    @classmethod
    def collapse(cls, operation, predicate, *terms):
        return cls.call(operation, cls.map(predicate, *terms))




class LogicalExpression(ConcreteSequence, Logical):
    def map(self, predicate):
        """
        Does not map-in place, IE treats this object as an immutable.
        eg.
        new_logical = logical.map(callable)
        """
        
        # cls = type(self)
        # terms = (interfaces._map(term, predicate) for term in self)
        # return cls(*(terms))  # construct new one
        return Logical.map(predicate, self)

    def call(self):
        # terms = (interfaces._call(term) for term in self)
        # return self.operation(*terms)
        return Logical.call(self.operation, self)

    def collapse(self, predicate=bool):
        """
        @type: predicate: Optional[Callable]
        @rtype: LogicalExpression
        """
        return self.map(predicate).call()


    def __str__(self):
        return logical_name.length_dispatch(self)(self)

    def __repr__(self):
        return str.format(
            "<{name}: operation={operation}, terms={terms}>",
            name=type(self).__name__,
            operation=self.operation.__name__,
            terms=", ".join(repr(term) for term in self)
        )

    def __call__(self):
        return self.operation(*self)





class LogicalIntersection(LogicalExpression):
    # def operation(self, *terms):
    #     return support.Intersection(*terms)
    operation = support.Intersection

class LogicalUnion(LogicalExpression):
    # def operation(self, *terms):
    #     return support.Union(*terms)
    operation = support.Union
    

class LogicalDifference(LogicalExpression):
    # def operation(self, *terms):
    #     return support.Difference(*terms)
    operation = support.Difference


class LogicalAtom(LogicalExpression):
    """
    Rewrites some functions not to invoke operation.
    """
    # def __init__(self, value):
    #     """
    #     Expects a single value.
    #     """
    #     super(LogicalAtom, self).__init__(value)

    operation = None

    def __init__(self, value):
        self.terms = value
    def __iter__(self):
        yield self.terms

    def call(self):
        return self.terms[0]

    def __repr__(self):
        return str.format(
            "<{name}: {terms}>",
            name=type(self).__name__,
            terms=repr(self.terms[0])
        )

    def __str__(self):
        return str(iter(self).next())


