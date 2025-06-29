import collections

from .patterns import Pattern


class LifeGrid:

    def __init__(self, pattern: Pattern) -> None:
        self.pattern = pattern

    def evolve(self) -> None:
        neighbors = [
            (-1, -1),
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        stay_live = {
            cell
            for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        new_live = {cell
                    for cell, num in num_neighbors.items()
                    if num == 3} - self.pattern.alive_cells

        self.pattern.alive_cells = stay_live | new_live

    def __str__(self) -> str:
        return (
            f"{self.pattern.name}:\nAlive cells -> {sorted(self.pattern.alive_cells)}"
        )
