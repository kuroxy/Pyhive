from typing import Self


class Node:
    """A node is just a component that can link with other nodes.
    This will be used as the base for each creature.
    """
    inverse_neighbour_index = [3, 4, 5, 0, 1, 2, 7, 6]

    def __init__(self, name: str, player: int) -> None:
        """Initizlize A node

        Args:
            name (str): The type of creature this is.
            player (int): player 0 or 1 who's tile this is.
        """
        self.name = name
        self.player = player
        self.neighbours = [None for _ in range(8)]

    def set_neighbour(self, neighbour: Self, neighbour_index: int):
        """Connects this Node with the given neighbour node on a side.

        Args:
            neighbour (Self): The node to connect to
            neighbour_index (int): Which side of this tile the neighbour will border
        """
        if neighbour_index < 0 or neighbour_index >= 8:
            raise "FUCK YOU IDIOT there can't be more neighbours"
        reverse_index = Node.inverse_neighbour_index[neighbour_index]

        self.neighbours[neighbour_index] = neighbour
        neighbour.neighbours[reverse_index] = self

    def remove_neighbour(self, neighbour_index: int):
        """Removes the connection between this and the side given

        Args:
            neighbour_index (int): Which neighbour side we want to remove
        """
        if neighbour_index < 0 or neighbour_index >= 8:
            raise "FUCK YOU IDIOT there can't be more neighbours"

        if not self.neighbours[neighbour_index]:
            return

        reverse_index = Node.inverse_neighbour_index[neighbour_index]
        neighbour = self.neighbours[neighbour_index]

        self.neighbours[neighbour_index] = None
        neighbour.neighbours[reverse_index] = None
