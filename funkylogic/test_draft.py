import unittest

from funkylogic import draft
from funkylogic import interfaces
from funkylogic import support

class DraftTests(unittest.TestCase):
    def test_basic(self):

        atom = draft.LogicalAtom('b')
        union = draft.LogicalUnion('aba', 'baba')

        self.assertEqual(tuple(atom), ('b', ))
        self.assertEqual(atom.terms, 'b')
        self.assertEqual(tuple(union), ('aba', 'baba'))
        self.assertEqual(union.terms, ('aba', 'baba'))

    def test_deep(self):
        """
        Compare union of atoms vs union of non-atoms.
        This will not clear at first, and may take some work to get
        it to work.
        """
        atom1 = draft.LogicalAtom('a')
        atom2 = draft.LogicalAtom('b')
        atoms = draft.LogicalUnion(atom1, atom2)
        union = draft.LogicalUnion('a', 'b')

        self.assertEqual(tuple(atoms), tuple(union))
        self.assertEQual(atoms, union)


class InterfaceTests(unittest.TestCase):
    def test_isinstance(self):
        from interfaces import _IS_LOGICAL
        
        self.assertFalse(_IS_LOGICAL(draft.LogicalExpression))
        self.assertFalse(_IS_LOGICAL(draft.LogicalUnion))
        self.assertTrue(_IS_LOGICAL(draft.LogicalUnion(1)))
        self.assertFalse(_IS_LOGICAL(draft.ConcreteSequence))

    def test_issubclass(self):
        is_logical = lambda obj: issubclass(obj, interfaces.LogicalInterface)

        self.assertTrue(is_logical(draft.LogicalExpression))
        self.assertTrue(is_logical(draft.LogicalUnion))
        self.assertFalse(is_logical(draft.ConcreteSequence))

        self.assertRaises(TypeError, is_logical, draft.LogicalUnion(1))
