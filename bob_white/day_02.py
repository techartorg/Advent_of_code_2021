start = [0, 0]

for line in open("day_02_input.txt"):
    if line.startswith("forward"):
        start[0] += int(line.split()[1])
    elif line.startswith("down"):
        start[1] += int(line.split()[1])
    elif line.startswith("up"):
        start[0] -= int(line.split()[1])
print(start[0] * start[1])

depth = 0
horizontal = 0
aim = 0
for line in open("day_02_input.txt"):
    if line.startswith("down"):
        aim += int(line.split()[1])
    if line.startswith("up"):
        aim -= int(line.split()[1])
    if line.startswith("forward"):
        horizontal += int(line.split()[1])
        depth += aim * int(line.split()[1])
print(depth * horizontal)
