from collections import deque


class Node(object):
    def __init__(self, name: str):
        self.name = name
        self.is_small = name.islower()
        self.children: list[Node] = []


def main():
    with open("inputs/day_12.txt", 'r') as f:
        start, end = parse_inputs(f.read())

    print(f"Part One: {solve(start, end, 0)}")
    print(f"Part Two: {solve(start, end, 1)}")


def parse_inputs(inputs: str) -> tuple[Node, Node]:
    nodes = {}

    for line in inputs.splitlines():
        lhs, rhs = line.split("-")
        if lhs not in nodes:
            nodes[lhs] = Node(lhs)

        if rhs not in nodes:
            nodes[rhs] = Node(rhs)

        nodes[lhs].children.append(nodes[rhs])
        nodes[rhs].children.append(nodes[lhs])

    return nodes["start"], nodes["end"]


def solve(start: Node, end: Node, aloud_smalls: int) -> int:
    routes = deque([([start], 0)])
    count = 0

    while routes:
        route, small_count = routes.popleft()
        node = route[-1]

        if node == end:
            count += 1
            continue

        if node.is_small and sum(i == node for i in route) > 1:
            if small_count >= aloud_smalls or node == start:
                continue

            small_count += 1

        for connection in node.children:
            next_route = route[:]
            next_route.append(connection)
            routes.append((next_route, small_count))

    return count


if __name__ == '__main__':
    main()
