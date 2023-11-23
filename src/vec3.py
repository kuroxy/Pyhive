
class Vec3:
    neighbours = [[0, 1, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0],
                  [-1, 0, 0], [-1, 1, 0], [0, 0, 1], [0, 0, -1]]

    def __init__(self, plist: list) -> None:
        self._poslist = [0, 0, 0]
        if len(plist) == 3:
            self._poslist = plist

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return self._poslist == other._poslist
        return False

    def __hash__(self):
        return hash(f"{self.x}{self.y}{self.z}")

    def get_neighbours(self):
        neighs = []
        for pos in Vec3.neighbours:
            neighs.append(Vec3([pos[0]+self.x, pos[1]+self.y, pos[2]+self.z]))
        return neighs

    @property
    def x(self):
        return self._poslist[0]

    @x.setter
    def x(self, value: int):
        self._poslist[0] = value

    @property
    def y(self):
        return self._poslist[1]

    @y.setter
    def y(self, value: int):
        self._poslist[1] = value

    @property
    def z(self):
        return self._poslist[2]

    @z.setter
    def z(self, value: int):
        self._poslist[2] = value
