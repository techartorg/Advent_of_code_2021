positions = [int(v) for v in "16,1,2,0,4,2,7,1,2,14".split(",")]
positions = [int(v) for v in open("day_07_input.txt").read().split(",")]
moves: list[tuple[int, int]] = []
for i in range(min(positions), max(positions) + 1):
    cost = sum(abs(v - i) for v in positions)
    moves.append((cost, i))

print(min(moves))

moves.clear()
for i in range(min(positions), max(positions) + 1):
    cost = sum(sum(range(abs(v - i) + 1)) for v in positions)
    moves.append((cost, i))

print(min(moves))
