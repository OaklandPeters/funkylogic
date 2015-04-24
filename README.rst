funky-logic
================

Synopsis
--------
Functional-programming based classes for Python classes supporting logical operations.
Useful in cases when more specialized parsing might otherwise be needed, such as `pyparsing (https://pypi.python.org/pypi/pyparsing)`_.

Movtivation
-------------
. . . this needs an actual description of the motivation of this project.


Personal Movtivation
----------------------
I found myself needing to be able to build logical statements (For example: `A or B and not C`; `Union[Intersection[Sequence, Not[str]], Iterator]), and then be able to apply (`map`) a function across the elements of those statements, before evaluating the logic. Reimplementing was messy, and got tedious.



Code Example
------------
. . . write a code example, after the library is prototyped.

.. code:: python

    import funkylogic

    class Union(funkylogic.LogicalIntersection):
        pass

    # . . .    


Installation
------------
. . . Provide code examples and explanations of how to get the project.

Contributors
------------
Oakland John Peters.

License
-----------
Copyright MIT 2014.
