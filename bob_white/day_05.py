from collections import defaultdict
vals = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')
vals = [l.strip() for l in open('day_05_input.txt').readlines()]
grid = defaultdict(int)
for line in vals:
    v1, v2 = line.split(' -> ')
    x1, x2, y1, y2 = map(int, v1.split(',') + v2.split(','))
    # print(x1, x2, y1, y2)
    if x1 == y1:
        start, end = sorted((x2, y2))
        for v in range(start, end + 1):
            grid[(x1, v)] += 1
    elif x2 == y2:
        start, end = sorted((x1, y1))
        for v in range(start, end + 1):
            grid[(v, x2)] += 1

print(sum(v > 1 for v in grid.values()))

grid = defaultdict(int)
for line in vals:
    v1, v2 = line.split(' -> ')
    x1, x2, y1, y2 = map(int, v1.split(',') + v2.split(','))

    if x1 == y1:
        start, end = sorted((x2, y2))
        for v in range(start, end + 1):
            grid[(x1, v)] += 1
    elif x2 == y2:
        start, end = sorted((x1, y1))
        for v in range(start, end + 1):
            grid[(v, x2)] += 1
    elif abs(x1-y1) == abs(x2 - y2):
        start, end = sorted((x2, y2))
        for v in range(abs(x1-y1)+1):
            if x1 < y1 and x2 < y2:
                grid[(x1+v, x2+v)] += 1
            elif y1 < x1 and y2 < x2:
                grid[(y1+v, y2+v)] += 1
            elif x1 < y1 and y2 < x2:
                grid[(x1+v, x2-v)] += 1
            elif x2 < y2 and y1 < x1:
                grid[(x1-v, x2+v)] += 1

print(sum(v > 1 for v in grid.values()))
# print(grid)