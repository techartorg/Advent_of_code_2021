from collections import defaultdict


example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split(
    "\n"
)

data = [line.strip().split("-") for line in open("day_12_input.txt")]
# data = [line.strip().split("-") for line in example]
paths: defaultdict[str, list[str]] = defaultdict(list)
for first, second in data:
    paths[first].append(second)
    paths[second].append(first)


def get_count_part1(path: str, visited: set[str], count: int = 0) -> int:
    if path == "end":
        return count + 1

    # Can't backtrack to lower case areas
    if path.islower() and path in visited:
        return count

    visited.add(path)
    for road in paths[path]:
        # each branch needs it own copy of visited nodes
        count = get_count_part1(road, visited.copy(), count)

    return count


def get_count_part2(path: str, visited: defaultdict[str, int], count: int = 0) -> int:
    if path == "end":
        return count + 1

    # Backtrack rules are more complex now
    if path.islower() and visited[path]:
        # Can't go back to start
        if path == "start":
            return count
        # Can only go back to one lower case node
        elif any(visit.islower() and visited[visit] > 1 for visit in visited):
            return count

    visited[path] += 1
    for pth in paths[path]:
        # each branch needs it own copy of visited nodes
        count = get_count_part2(pth, visited.copy(), count)
    return count


print(get_count_part1("start", set()))
print(get_count_part2("start", defaultdict(int)))
