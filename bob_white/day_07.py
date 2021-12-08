positions = [int(v) for v in "16,1,2,0,4,2,7,1,2,14".split(",")]
positions = [int(v) for v in open("day_07_input.txt").read().split(",")]
moves: list[tuple[int, int]] = []
for i in range(min(positions), max(positions) + 1):
    cost = sum(abs(v - i) for v in positions)
    moves.append((cost, i))

print(min(moves))


def get_cost(position: int, move_to: int, *, _cache: dict[int, int] = {}) -> int:
    v = abs(position - move_to) + 1
    if v not in _cache:
        _cache[v] = sum(range(v))
    return _cache[v]


moves.clear()
for i in range(min(positions), max(positions) + 1):
    cost = sum(get_cost(v, i) for v in positions)
    moves.append((cost, i))

print(min(moves))
