from __future__ import annotations

from heapq import heapify, heappop, heappush
from typing import Iterator

Pt = tuple[int, int]


class Node(object):
    def __init__(self, position: Pt, cost: int):
        self.position: Pt = position
        self.cost: int = cost
        self.start_cost: int = cost
        self.parent: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.position}, {self.cost})"

    def __lt__(self, other: Node) -> bool:
        return self.cost < other.cost if self.cost == other.cost else self.position < other.position


Grid = dict[(int, int), Node]


def main():
    with open("inputs/day_15.txt", 'r') as f:
        grid_one, size_one = parse_grid(f.read())

    grid_two, size_two = repeated(grid_one, size_one, 5)

    print(f"Part One: {solve(grid_one, size_one)}")
    print(f"Part Two: {solve(grid_two, size_two)}")


def parse_grid(inputs: str) -> tuple[Grid, Pt]:
    lines = inputs.splitlines()
    grid = {}
    for y, row in enumerate(lines):
        for x, cost in enumerate(row):
            grid[(x, y)] = Node((x, y), int(cost))
    return grid, (len(lines[0]), len(lines))


def repeated(grid: Grid, size: Pt, repeats: int) -> tuple[Grid, Pt]:
    new_size = (size[0] * repeats, size[1] * repeats)
    new_grid = {}

    for x in range(new_size[0]):
        for y in range(new_size[1]):
            cost = grid[(x % size[0], y % size[1])].cost
            repeat_count = (x // size[0] + y // size[1]) - 1
            new_grid[(x, y)] = Node((x, y), ((cost + repeat_count) % 9) + 1)

    return new_grid, new_size


def draw_grid(grid: Grid, size: Pt, path: list[Node] = None):
    path = set(path) if path else set()

    for y in range(size[1]):
        line = "".join(f"\033[91m{node.start_cost}\33[0m" if (node := grid[(x, y)]) in path else f"\033[90m{node.start_cost}\33[0m" for x in range(size[0]))
        print(line)


def find_path(grid: Grid, start: Node, target: Node) -> list[Node] | None:
    closed_set = set()
    open_set = [(0, start)]
    heapify(open_set)

    while open_set:
        cost, node = heappop(open_set)

        if node == target:
            return retrace_path(start, target)

        if node in closed_set:
            continue

        closed_set.add(node)

        for neighbour in get_neighbours(grid, node):
            if neighbour in closed_set:
                continue

            neighbour.cost += cost
            neighbour.parent = node
            heappush(open_set, (neighbour.cost, neighbour))


def get_neighbours(grid: Grid, node: Node) -> Iterator[Node]:
    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if neighbour := grid.get((node.position[0] + x, node.position[1] + y)):
            yield neighbour


def retrace_path(head: Node, tail: Node) -> list[Node]:
    path = []
    current = tail

    while current != head:
        path.append(current)
        current = current.parent

    path.append(head)
    path.reverse()

    return path


def solve(grid: Grid, size: Pt) -> int:
    start = grid[(0, 0)]
    target = grid[(size[0]-1, size[1]-1)]
    path = find_path(grid, start, target)
    # draw_grid(grid, size, path)
    return path[-1].cost


if __name__ == '__main__':
    main()
