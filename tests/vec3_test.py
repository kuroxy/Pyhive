from src.vec3 import Vec3
import unittest


class TestNodeMethods(unittest.TestCase):
    def test_init_getters(self):
        v = Vec3([1, 2, 3])

        self.assertEqual(v._poslist, [1, 2, 3])

        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_equal(self):
        v = Vec3([1, 2, 3])
        v2 = Vec3([1, 2, 3])

        self.assertEqual(v, v)
        self.assertEqual(v, v2)

    def test_unequal(self):
        v = Vec3([1, 2, 3])
        v2 = Vec3([1, 2, 3])
        self.assertNotEqual(v, v2)

    def test_get_neighs(self):
        v = Vec3([0, 0, 0])
        neighs = [[0, 1, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0],
                  [-1, 0, 0], [-1, 1, 0], [0, 0, 1], [0, 0, -1]]
        neighsvec3 = [Vec3(l) for l in neighs]
        self.assertEqual(v.get_neighbours(), neighsvec3)

    def test_get_neighs2(self):
        v = Vec3([1, 2, 3])
        neighs = [[1, 3, 3], [2, 2, 3], [2, 1, 3], [1, 1, 3],
                  [0, 2, 3], [0, 3, 3], [1, 2, 4], [1, 2, 2]]
        neighsvec3 = [Vec3(l) for l in neighs]

        self.assertEqual(v.get_neighbours(), neighsvec3)

    def test_hash(self):
        v = Vec3([1, 2, 3])
        v2 = Vec3([1, 2, 3])
        v3 = Vec3([2, 7, 3])

        self.assertEqual(v.__hash__(), v2.__hash__())
        self.assertNotEqual(v.__hash__(), v3.__hash__())


if __name__ == '__main__':
    unittest.main()
