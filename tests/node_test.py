from src.node import Node
import unittest


class TestNodeMethods(unittest.TestCase):
    def test_init(self):
        nodeA = Node()
        self.assertEqual(nodeA.neighbours, [
                         None, None, None, None, None, None, None, None])

    def test_add(self):
        nodeA = Node()
        nodeB = Node()

        nodeA.set_neighbour(nodeB, 0)

        self.assertEqual(nodeA.neighbours, [
                         nodeB, None, None, None, None, None, None, None])
        self.assertEqual(nodeB.neighbours, [
                         None, None, None, nodeA, None, None, None, None])

    def test_remove(self):
        nodeA = Node()
        nodeB = Node()

        nodeA.set_neighbour(nodeB, 0)

        nodeA.remove_neighbour(0)

        self.assertEqual(nodeA.neighbours, [
                         None, None, None, None, None, None, None, None])
        self.assertEqual(nodeB.neighbours, [
                         None, None, None, None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()
